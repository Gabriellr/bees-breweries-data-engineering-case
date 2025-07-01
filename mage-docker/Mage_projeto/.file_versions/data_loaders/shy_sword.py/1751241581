from mage_ai.data_preparation.decorators import data_loader
from pyspark.sql import SparkSession
import logging

@data_loader
def load_virtualized_parquet(*args, **kwargs):
    """
    Cria uma view temporária no Spark com base em arquivos Parquet no S3.
    Permite que os dados sejam consultados via Spark SQL como uma tabela virtual.
    """

    # Nome do bucket S3 e prefixo (subpasta opcional)
    bucket_name = 'db-inbev-gold-layer'
    prefix = kwargs.get('folder_name', '')  # Ex: '2025-06-29/' ou ''

    # Caminho completo no S3
    s3_path = f"s3a://{bucket_name}/{prefix}*"

    # Inicia a sessão Spark
    spark = SparkSession.builder \
        .appName("VirtualizeParquet") \
        .getOrCreate()

    logging.info(f"📥 Lendo arquivos Parquet de {s3_path}")

    # Lê os dados e registra uma view temporária
    df = spark.read.parquet(s3_path)
    df.createOrReplaceTempView("breweries_virtual_view")

    logging.info("✅ View temporária criada: breweries_virtual_view")

    return df