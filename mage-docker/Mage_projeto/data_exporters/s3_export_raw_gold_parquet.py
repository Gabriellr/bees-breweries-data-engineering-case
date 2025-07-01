from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from pandas import DataFrame
from os import path
import logging
import time
from datetime import datetime  # necessário para pegar a data de hoje

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_s3(df: DataFrame, **kwargs) -> None:
    """
    Exporta DataFrame para um bucket S3 no formato Parquet.
    Realiza até 3 tentativas em caso de erro.
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Bucket e caminho do arquivo
    bucket_name = 'db-inbev-gold-layer'
    folder_name = datetime.today().strftime('%Y-%m-%d')
    s3_prefix = f"{folder_name}"
    object_key = f"{s3_prefix}/breweries_gold.parquet"

    max_retries = 3
    attempt = 0

    while attempt < max_retries:
        try:
            attempt += 1
            logging.info(f" Tentativa {attempt} de exportar para S3...")

            S3.with_config(ConfigFileLoader(config_path, config_profile)).export(
                df,
                bucket_name,
                object_key,
            )

            logging.info(f" Arquivo exportado com sucesso para s3://{bucket_name}/{object_key}")
            break  # Sucesso → encerra loop
        except Exception as e:
            logging.error(f"Erro ao exportar para S3 (tentativa {attempt}): {e}")
            if attempt < max_retries:
                time.sleep(2)  # Aguarda 2 segundos antes da próxima tentativa
            else:
                logging.critical("Todas as tentativas de exportação falharam.")
                raise  # Relevanta a exceção para Mage registrar como erro
