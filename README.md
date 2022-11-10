# Projeto Final Extensão-Airflow

## Objetivo:

- Criação de um projeto com Airflow, utilizando os conhecimentos adquiridos durante o curso de extensão de 15 dias oferecido pela SoulCode Academy.
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


## Estrutura do docker-compose.yaml

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
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=380px > </div>
 

## Estrutura da DAG

- Import das bibliotecas necessárias;

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=380px > </div>

- Definição de alguns argumentos;

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=380px > </div>

- A primeira função (extrair_dados), responsável por extrair os dados pela URL informada e guardar o dataset sem tratamento dentro da pasta dados_brutos

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=380px > </div>

- A segunda função (tratamento_dados), responsável por ler e tratar os dados

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=380px > </div>

- A terceira função (exportacao_dados), converteu o dataset tratado em formato csv e parquet, os quais foram armazenados na pasta de dados_tratados

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=380px > </div>

- Instanciamento da DAG

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=380px > </div>

- Definição das Tasks

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=380px > </div>

- Definição das Dependências

<div align="center">
<img src="https://user-images.githubusercontent.com/83531935/200970950-441d2825-0f50-41b8-8885-44759feccf7b.gif" width=380px > </div>


