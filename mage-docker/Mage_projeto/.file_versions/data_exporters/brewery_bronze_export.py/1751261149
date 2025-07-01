# Importa utilitários do Mage.ai para caminho do repositório e configuração do S3
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from pandas import DataFrame
from os import path
import time  # Para controlar tempo entre retentativas
import traceback  # Para imprimir rastros de erro completos

# Importa decorador apenas se ainda não tiver sido carregado (usado no ambiente do Mage)
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_s3(df: DataFrame, **kwargs) -> None:
    """
    Exporta dados do DataFrame para um bucket S3, com até 3 tentativas em caso de falha.
    A configuração do acesso ao S3 deve estar definida em 'io_config.yaml'.
    """

    # Caminho do arquivo de configuração e perfil
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Nome do bucket e chave do objeto onde os dados serão salvos
    bucket_name = 'db-inbev-bronze-layer'
    object_key = 'breweries_raw.json'

    # Até 3 tentativas para exportar os dados ao S3
    max_attempts = 3
    attempt = 0
    success = False

    while attempt < max_attempts and not success:
        try:
            # Realiza a exportação usando a configuração do Mage.ai
            S3.with_config(ConfigFileLoader(config_path, config_profile)).export(
                df,
                bucket_name,
                object_key,
            )

            print(f"[Sucesso] Dados exportados com sucesso para o bucket: s3://{bucket_name}/{object_key}")
            success = True  # Marca a operação como bem-sucedida

        except Exception as e:
            attempt += 1
            print(f"[Erro] Tentativa {attempt}/{max_attempts} falhou ao exportar para S3.")
            traceback.print_exc()  # Imprime o traceback completo do erro para debug
            time.sleep(2)  # Aguarda 2 segundos antes de tentar novamente

            # Se falhar nas 3 tentativas, lança o erro final
            if attempt == max_attempts:
                raise RuntimeError(f"[Falha Crítica] Não foi possível exportar os dados para s3://{bucket_name}/{object_key} após {max_attempts} tentativas.") from e