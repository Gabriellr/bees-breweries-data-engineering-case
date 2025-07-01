# Importa utilitários do Mage.ai para configuração do projeto e acesso ao S3
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from os import path
import time  # Para pausa entre tentativas

# Importa os decoradores apenas se ainda não estiverem carregados (útil no Mage.ai)
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_s3_bucket(*args, **kwargs):
    """
    Carrega dados do S3 definidos em um bucket e chave específicos.
    Realiza até 3 tentativas em caso de erro com delay entre elas.
    A configuração de acesso deve estar em 'io_config.yaml'.
    """

    # Caminho do arquivo de configuração e perfil do Mage
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # Bucket e objeto (caminho do arquivo) no S3
    bucket_name = 'db-inbev-bronze-layer'
    object_key = 'breweries_raw.json'

    # Parâmetros para controle de tentativas
    max_retries = 3
    delay_seconds = 5  # tempo entre tentativas em segundos

    last_exception = None  # Guarda a última exceção para relançar se necessário

    for attempt in range(1, max_retries + 1):
        try:
            # Tenta carregar os dados do S3
            print(f"Tentando carregar dados do S3 (tentativa {attempt}/{max_retries})...")
            df = S3.with_config(ConfigFileLoader(config_path, config_profile)).load(
                bucket_name,
                object_key,
            )
            print(f"[Sucesso] Dados carregados de s3://{bucket_name}/{object_key}")
            return df  # Sucesso: retorna o DataFrame
        except Exception as e:
            # Em caso de falha, exibe o erro e espera antes de tentar novamente
            last_exception = e
            print(f"[Erro] Tentativa {attempt} falhou ao carregar do S3: {e}")
            if attempt < max_retries:
                print(f"Aguardando {delay_seconds} segundos antes da próxima tentativa...")
                time.sleep(delay_seconds)
            else:
                # Última tentativa falhou: levanta erro crítico
                print("[Falha crítica] Todas as tentativas de leitura falharam.")
                raise RuntimeError(f"Erro ao carregar dados do S3 após {max_retries} tentativas.") from e

    # Segurança: relança a última exceção (não deveria chegar aqui)
    raise last_exception


@test
def test_output(output, *args) -> None:
    """
    Teste para garantir que os dados foram carregados corretamente.
    Suporta tanto DataFrame Pandas quanto Spark.
    """
    assert output is not None, 'O output está vazio'

    import pandas as pd
    if isinstance(output, pd.DataFrame):
        assert not output.empty, 'O DataFrame Pandas está vazio'
    else:
        # Se não for Pandas, assume que é Spark
        assert output.count() > 0, 'O DataFrame Spark está vazio'
