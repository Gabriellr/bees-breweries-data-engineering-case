from mage_ai.data_preparation.decorators import data_loader
from pyspark.sql import SparkSession
import logging

@data_loader
def load_virtualized_parquet(*args, **kwargs):
    """
    Cria uma view temporária no Spark com base em arquivos Parquet no S3.
    Permite que os dados sejam consultados via Spark SQL como uma tabela virtual.
    """

    bucket_name = 'db-inbev-gold-layer'
    prefix = kwargs.get('folder_name', '')  # Ex: '2025-06-29/' ou ''
    s3_path = f"s3a://{bucket_name}/{prefix}*"

    logging.info(f"📥 Virtualizando arquivos Parquet: {s3_path}")

    spark = SparkSession.builder \
        .appName("VirtualizeParquet") \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.520") \
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
        .getOrCreate()

    try:
        df = spark.read.parquet(s3_path)
        df.createOrReplaceTempView("breweries_virtual_view")
        logging.info("✅ View temporária criada com nome: breweries_virtual_view")
        return df
    except Exception as e:
        logging.error(f"❌ Erro ao virtualizar arquivos Parquet: {e}")
        raise
