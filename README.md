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

2. **Instale e inicie o Docker**
   Certifique-se de que o Docker Desktop está instalado e em execução na sua máquina.
Com o Docker pronto, navegue até a raiz do projeto mage-docker e execute o seguinte comando para iniciar o Mage.ai:

   ```bash
   docker-compose up --build

 2. **Executando o Pipeline pela Interface do Mage.ai**

Para executar manualmente seu pipeline no Mage.ai, siga os passos abaixo:

1. Acesse a interface web em: [http://localhost:6789](http://localhost:6789) ou [http://localhost:6789/pipelines/elt_proj_breweries/triggers](http://localhost:6789/pipelines/elt_proj_breweries/triggers) 

2. No menu lateral, clique na aba **Pipelines**.

3. Selecione o pipeline desejado (por exemplo: `elt_proj_breweries`).

4. Na página do pipeline, vá até a aba **Triggers**.

5. Clique no botão **`Run@once`** para iniciar a execução manual do pipeline.

![mageai_run](https://github.com/user-attachments/assets/9360bb6b-a802-41e6-8875-d8119212d7dc)

Você poderá **acompanhar o progresso**, **verificar os logs** e **analisar os resultados em tempo real** diretamente pela interface gráfica.

---
