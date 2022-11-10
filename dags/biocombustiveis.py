from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.models.baseoperator import chain
import pandas as pd
import requests

# Definindo alguns argumentos básicos
default_args = {
    'owner':'treinamento_dag',
    'retry': 2,
    'retry_delay': timedelta(minutes=3),
    'email_on_failure': True,
    'email_on_retry': True,
    'email':'kkaori146@gmail.com'    
}

#Função para extrair dados:
def extrair_dados():
    url = 'https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos-painel-de-produtores-de-derivados-producao-de-biocombustiveis/biodiesel_dadosabertos_csv_materiaprima.csv/@@download/file/Biodiesel_DadosAbertos_CSV_Mat%C3%A9riaPrima.csv'
    x = requests.get(url)
    open('dadosbrutos/Biodiesel_DadosAbertos_CSV_Mat%C3%A9riaPrima.csv', 'wb').write(x.content)

#Leitura e Tratamento dos dados:
def tratamento_dados():
    df = pd.read_csv('dadosbrutos/Biodiesel_DadosAbertos_CSV_Mat%C3%A9riaPrima.csv', sep=',')

    # Definição dos Tipos de Dados das Colunas
    df['Mês/Ano'] = df['Mês/Ano'].astype(str)
    df['Razão Social'] = df['Razão Social'].astype(str)
    df['Estado'] = df['Estado'].astype(str)
    df['Município'] = df['Município'].astype(str)
    df['Produto'] = df['Produto'].astype(str)
    df['Quantidade (m³)'] = df['Quantidade (m³)'].astype(float)

    # Replace da inconsistência encontrada na coluna "Produto"
    df['Produto'] = df['Produto'].apply(lambda x: x.replace('(ELAEIS GUINEENSIS OU ELAEIS O', '(ELAEIS GUINEENSIS OU ELAEIS O)'))
    
    # Eliminação da coluna Região (o dataset traz outras especificações para melhor localização)
    df = df.drop(['Região'], axis=1)

    # Uso de slice para corrigir inconsistências na coluna "Mês/Ano"
    df["Mês/Ano"] = df["Mês/Ano"].str.slice(0 ,7)

    # Tratamento das inconsistências, utilizando o pandas
    df.replace(["NaN", "nan", " ", "", "NAN", "NA"], pd.NA, inplace = True)

    return df

# Salvando o dataset final em formato csv e parquet
def exportacao_dados(**kwargs):

# Intercomunicação das tasks com XCOM (com Postgres)
    ti=kwargs['ti']
    df = ti.xcom_pull(task_ids='tratamento_dados')

# Conversão do dataset em arquivos csv e parquet
    df.to_csv('dadostratados/bioenergia.csv',index=False)
    df.to_parquet('dadostratados/bioenergia.parquet', index=False)

# Salva o arquivo em cvs e parquet com a quatidade total de derivados por estado
def soma_estado():
  dfsoma_produto = pd.read_csv('dadostratados/bioenergia.csv', sep=',')
  dfsoma_produto = dfsoma_produto.groupby(['Estado', 'Produto'])['Quantidade (m³)'].sum().reset_index()

# Conversão do dataset em arquivos csv e parquet
  dfsoma_produto.to_csv('dadostratados/estado_produto.csv',index=False)
  dfsoma_produto.to_parquet('dadostratados/estado_produto.parquet', index=False)


# Instanciando a DAG:
with DAG(
    dag_id='biocombustiveis_dag',
    start_date = days_ago(1),
    schedule_interval="@daily",
    default_args = default_args,
    catchup=True,
    max_active_runs=2) as dag:

# Definição das Tasks
  start = EmptyOperator(task_id='Start')

  extrair_dados = PythonOperator(
      task_id = 'extrair_dados',
      python_callable = extrair_dados
  )

  tratamento_dados = PythonOperator(
    task_id = 'tratamento_dados',
    python_callable = tratamento_dados
  )

  exportacao_dados = PythonOperator(
    task_id = 'exportacao_dados',
    provide_context=True,
    python_callable = exportacao_dados
  )

  soma_estado = PythonOperator(
    task_id="soma_estado",
    python_callable=soma_estado
  )

  end = EmptyOperator(task_id='end')

# Definição das Dependências
chain(start, extrair_dados, tratamento_dados, exportacao_dados, soma_estado, end)