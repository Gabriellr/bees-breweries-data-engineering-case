# BEES Data Engineering – Breweries Case
 Este pipeline de dados, desenvolvido em Docker, realiza a extração de informações da API Open Brewery DB. Utilizando Apache Spark para processamento e transformação, e Mage.ai para orquestração, ele aplica a arquitetura Medallion para estruturar os dados em três camadas. Os dados são armazenados em um Data Lake na nuvem (AWS S3 ou Azure Blob Storage). Na camada Bronze, os dados brutos da API são salvos em formato Parquet; na camada Silver, são transformados e particionados por localização; e na camada Gold, os dados são agregados e enriquecidos com métricas como o número de cervejarias por tipo e região.

Tecnologias e Ferramentas

    Mage.ai – Orquestração do pipeline
    PySpark – Processamento distribuído
    Pandas – Manipulação de dados leves
    AWS S3 – Camadas do data lake
    boto3 – Integração programática com S3
    Docker – Containerização do ambiente
    
