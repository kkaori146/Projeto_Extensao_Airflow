# Projeto Final Extensão-Airflow
<div align='center'>
<p float="right">
  <img src="https://user-images.githubusercontent.com/83531935/200994962-fcbedd70-d397-44d2-8369-15fe14ba6259.png" width="190" />
 
  <img src="https://user-images.githubusercontent.com/83531935/200994945-fbe30288-68a4-433a-9d5b-37ffed81fabe.png" width="140" /> 
</p></div>

## Informações Gerais:

- Criação de um projeto com Airflow, utilizando os conhecimentos adquiridos durante o curso de extensão para o Processo Seletivo da Raízen.
- Duração da extensão de 15 dias oferecido pela SoulCode Academy.
- Foi realizado um tratamento e interpretação preliminar visando a utilização do Airflow.

## Fontes:

- ANP
https://www.gov.br/anp/pt-br

- KLM
https://news.klm.com/klm-further-expands-approach-for-sustainable-aviation-fuel/


## Sobre a Escolha do Dataset

- O Dataset traz informações entre os períodos de 2017 a 2022 de empresas, sua localização e a quantidade em m3 de derivados produzidos.

- Derivados como Óleo de Milho, Palma, Soja, Gordura Bovina que podem ser utilizados na produção e na pesquisa de formas de síntese de biocombustíveis (biodiesel).
    Exemplo: A utilização da Gordura de Boi é feita na produção de combustível para aviões. Algumas empresas como a KLM utiliza biocombustível produzido a partir de gordura de boi em alguns dos seus voos comerciais (atualmente mais de 190 voos).
    
## Ferramenta de Apoio

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200990110-1c050634-3048-4634-af85-6d2bf7599bc7.png" width=300px > </div>

- Arquivo do colab utilizado no projeto

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200991672-821482a5-0aec-46bb-9c82-58e5dbe4e3b0.png" width=1000px > </div>

## Estrutura do docker-compose.yaml

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200985753-cd457113-e248-4e38-be20-212e1db3069e.png" width=300px > </div>

- Na parte de environment build do Airflow foi adicionado um comando para habilitar o uso do xcom:
AIRFLOW__CORE__ENABLE_XCOM_PICKLING: 'true'

- E um comando foi desabilitado no environment build do Airflow, para a não criação de exemplos, economizando assim recursos da máquina:
AIRFLOW__CORE__LOAD_EXAMPLES: 'false'

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970210-c026031f-0b57-4076-ad34-b7d75c824677.gif" width=700px > </div>

- Em volumes foi criado os volumes para armazenamento dos dados brutos e tratados:
    - ./dados_brutos:/opt/airflow/dadosbrutos
    - ./dados_tratados:/opt/airflow/dadostratados

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=350px > </div>
 
## Estrutura da DAG

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200988779-e72c1585-0015-4c7c-ba71-88eca955bf55.png" width=800px> </div>

- Import das bibliotecas necessárias;

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200978277-51073d0a-9266-4051-ab51-6581db362734.png" width=380px> </div>
          
- Definição de alguns argumentos

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200974685-d7a38dd9-16b0-4946-8a06-c894b9f5d655.gif" width=340px > </div>

                                                                                                                
- A primeira função (extrair_dados), responsável por extrair os dados pela URL informada e guardar o dataset sem tratamento dentro da pasta dados_brutos


<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200979650-38e853c6-eb52-4f3b-82c4-82c8e50729a1.png" width=1000000px > </div>


- A segunda função (tratamento_dados), responsável por ler e tratar os dados


<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200974684-2cb6ad85-641a-486d-8076-aaa88ab7cada.gif" width=900px > </div>


- A terceira função (exportacao_dados), converteu o dataset tratado em formato csv e parquet, os quais foram armazenados na pasta de dados_tratados


<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200974681-a1a95a4c-8024-484c-885f-9695b0f9bae9.gif" width=380px > </div>

- Instanciamento da DAG

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200974677-efcf731c-646b-43d0-b6c5-6ced308245a8.gif" width=240px > </div>

- Definição das Tasks

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200975210-3cbdbe30-af6c-492c-8fde-68bab3b763e0.gif" width=340px > </div>

- Definição das Dependências

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200974686-0b928623-e89f-4f47-8b44-0b7a3e853c53.gif" width=500px > </div>

## Carregar o Airflow

- Comando para Inicialização rápida do Airflow

**_docker-compose up airflow-init_**

- Comando que agrega, cria e toma as modificações realizadas

**_docker-compose up_**

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200983371-419d82ac-0cdd-4fee-be84-b94d03d844f9.png" width=800px > </div>

## Execução das Tasks

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200989438-29a8b688-9e4b-48e6-995b-a0d231beac4a.png" width=800px > </div>




