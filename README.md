#Projeto Final Extensão-Airflow
<hr>

##Objetivo:
<hr>
- Criação de um projeto com Airflow, utilizando os conhecimentos adquiridos durante o curso de extensão de 15 dias oferecido pela SoulCode Academy.
- Foi realizado um tratamento e interpretação preliminar visando a utilização do Airflow.
<hr>

##Fontes:
<hr>
- ANP
https://www.gov.br/anp/pt-br

- KLM
https://news.klm.com/klm-further-expands-approach-for-sustainable-aviation-fuel/
<hr>

##Sobre a Escolha do Dataset
<hr>
- O Dataset traz informações entre os períodos de 2017 a 2022 de empresas, sua localização e a quantidade em m3 de derivados produzidos.

- Derivados como Óleo de Milho, Palma, Soja, Gordura Bovina que podem ser utilizados na produção e na pesquisa de formas de síntese de biocombustíveis (biodiesel).
    Exemplo: A utilização da Gordura de Boi é feita na produção de combustível para aviões. Algumas empresas como a KLM utiliza biocombustível produzido a partir de gordura de boi em alguns dos seus voos comerciais (atualmente mais de 190 voos).
<hr>

##Estrutura do docker-compose.yaml
<hr>
- Na parte de environment build do Airflow foi adicionado um comando para habilitar o uso do xcom:
AIRFLOW__CORE__ENABLE_XCOM_PICKLING: 'true'

- E um comando foi desabilitado no environment build do Airflow, para a não criação de exemplos, economizando assim recursos da máquina:
AIRFLOW__CORE__LOAD_EXAMPLES: 'false'

- Em volumes foi criado os volumes para armazenamento dos dados brutos e tratados:
    - ./dados_brutos:/opt/airflow/dados_brutos
    - ./dados_tratados:/opt/airflow/dados_tratados
<hr>
##Estrutura da DAG
<hr>
- Inicialmente foi feito o import das bibliotecas necessárias;
- Foi estabelecido um default_args com alguns argumentos;
- A primeira função (extrair_dados), foi responsável por extrair os dados pela URL informada e guardar o dataset sem tratamento dentro da pasta dados_brutos;
- A segunda função (tratamento_dados), foi responsável por ler e tratar os dados
- A terceira função (exportacao_dados), converteu o dataset tratado em formato csv e parquet, os quais foram armazenados na pasta de dados_tratados



