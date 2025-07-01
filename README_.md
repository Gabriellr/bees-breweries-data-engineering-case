## BEES Data Engineering – Breweries Case

Este pipeline de dados, desenvolvido em Docker, realiza a extração de informações da API Open Brewery DB. Utilizando Apache Spark para processamento e transformação, e Mage.ai para orquestração, ele aplica a arquitetura Medallion para estruturar os dados em três camadas.

Os dados são armazenados em um Data Lake na nuvem (AWS S3 ). Na camada Bronze, os dados brutos da API são salvos em formato Parquet; na camada Silver, são transformados e particionados por localização; e na camada Gold, os dados são agregados e enriquecidos com métricas como o número de cervejarias por tipo e região.

# Tecnologias e Ferramentas

- **Mage.ai** – Orquestração do pipeline  
- **PySpark** – Processamento distribuído  
- **Pandas** – Manipulação de dados leves  
- **AWS S3** – Camadas do data lake  
- **boto3** – Integração programática com S3  
- **Docker** – Containerização do ambiente  
    
 ##  Arquitetura de Pipeline

O pipeline foi desenvolvido com base na arquitetura **Medallion**, utilizando tecnologias modernas, escaláveis e com foco em boas práticas de engenharia de dados.

###  Estrutura em Camadas (Medallion)

A arquitetura organiza os dados em três camadas principais:

- **🔹 Bronze (Raw)**  
  Armazena os dados brutos coletados diretamente da API, sem transformações. Serve como fonte de verdade imutável.

- **🔸 Silver (Curated)**  
  Realiza a limpeza, normalização e enriquecimento dos dados. Salva em formato colunar (Parquet), particionado por país e região.

- **🥇 Gold (Analytics)**  
  Dados prontos para consumo analítico. Aqui, são geradas **agregações por tipo de cervejaria e localização**, otimizando performance para dashboards e relatórios.

![bees-brew drawio](https://github.com/user-attachments/assets/30379ef6-8a66-4e1f-bc69-9505c81358cc)

## Instalação

### Pré-requisitos

- Docker instalado na sua máquina (versão recomendada >= 20.x)

### Passos para rodar o projeto

### Passos para rodar o projeto

1. **Clone o repositório**

   Clone este projeto em sua máquina local:

   ```bash
   git clone https://github.com/Gabriellr/bees-breweries-data-engineering-case.git
   cd bees-breweries-data-engineering-case
   cd mage-docker

2. **Instale e inicie o Docker**
   Certifique-se de que o Docker Desktop está instalado e em execução na sua máquina.
Com o Docker pronto, navegue até a raiz do projeto mage-docker e execute o seguinte comando para iniciar o Mage.ai:

   ```bash
   docker-compose up --build

 3. **Executando o Pipeline pela Interface do Mage.ai**

Para executar manualmente seu pipeline no Mage.ai, siga os passos abaixo:

  1. Acesse a interface web em: [http://localhost:6789](http://localhost:6789) ou [http://localhost:6789/pipelines/elt_proj_breweries/triggers](http://localhost:6789/pipelines/elt_proj_breweries/triggers) 

  2. No menu lateral, clique na aba **Pipelines**.

  3. Selecione o pipeline desejado (por exemplo: `elt_proj_breweries`).

  4. Na página do pipeline, vá até a aba **Triggers**.

  5. Clique no botão **`Run@once`** para iniciar a execução manual do pipeline.
![mage6](https://github.com/user-attachments/assets/6a29ce5c-736d-4517-9004-7835fe192dff)



Você poderá **acompanhar o progresso**, **verificar os logs** e **analisar os resultados em tempo real** diretamente pela interface gráfica.

---
### Melhoria Recomendada: Observabilidade e Governança com AWS

O pipeline foi desenvolvido com ferramentas gratuitas e de código aberto (`Mage.ai`, `PySpark`, `Docker` e `AWS S3`), priorizando acessibilidade e fácil reprodutibilidade. No entanto, para ambientes corporativos ou produtivos, recomenda-se a adoção de serviços gerenciados da AWS que ampliam significativamente a **observabilidade**, **governança** e **eficiência operacional**:

- Monitoramento & Alertas:
  Utilizar o **Amazon CloudWatch** em conjunto com o **Amazon SNS** para monitorar falhas, tempos de execução e criar alertas automáticos em tempo real.

- Catálogo de Dados:
  Integrar o **AWS Glue Data Catalog** para registrar metadados das camadas Bronze, Silver e Gold, promovendo descoberta, versionamento e auditoria de dados.

- Virtualização de Dados:  
  Adotar o **Amazon Athena** para consultas SQL diretamente sobre os dados armazenados no S3, sem a necessidade de ETL ou cargas adicionais.

- Qualidade de Dados:  
  Incorporar ferramentas como **AWS Deequ** (Spark) ou **Amazon DataZone** para rastrear qualidade, integridade e regras de negócio nos dados de forma automatizada.
  
> *Esses recursos não foram utilizados nesta versão do projeto para manter o custo zero, mas são altamente recomendados em contextos com maior volume, criticidade e requisitos de compliance e escalabilidade.*
