from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
import boto3
from os import path
import logging

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


@data_loader
def delete_all_files_in_s3_bucket(*args, **kwargs):
    """
    Deleta todos os arquivos (incluindo subdiretórios) de um bucket S3.
    Use o parâmetro 'prefix' se quiser deletar apenas uma pasta (ex: '2025-06-30/').
    """

    bucket_name = 'db-inbev-bronze-layer'
    prefix = kwargs.get('prefix', '')  # Ex: '' para tudo, ou '2025-06-30/'

    s3_client = boto3.client('s3')

    try:
        paginator = s3_client.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

        deleted_files = 0
        for page in pages:
            if 'Contents' not in page:
                logging.info("Nenhum arquivo para deletar.")
                continue

            for obj in page['Contents']:
                key = obj['Key']
                logging.info(f"Deletando: {key}")
                s3_client.delete_object(Bucket=bucket_name, Key=key)
                deleted_files += 1

        logging.info(f"Deleção concluída: {deleted_files} arquivos removidos de s3://{bucket_name}/{prefix}")
        return f"{deleted_files} arquivos deletados de s3://{bucket_name}/{prefix}"

    except Exception as e:
        logging.error(f"Erro ao deletar arquivos do bucket: {str(e)}")
        raise