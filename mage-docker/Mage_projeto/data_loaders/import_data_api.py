# Importa os decoradores apenas se ainda não estiverem carregados (necessário no ambiente do Mage.ai)
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import requests
import time
from pyspark.sql import SparkSession

@data_loader
def load_data_from_api_spark(*args, **kwargs):
    url = "https://api.openbrewerydb.org/v1/breweries"
    all_data, page = [], 1

    # Loop para paginação da API
    while True:
        attempt = 0
        success = False
        # Tenta até 3 vezes fazer a requisição da página
        while attempt < 3 and not success:
            try:
                response = requests.get(f"{url}?per_page=200&page={page}", timeout=10)
                response.raise_for_status()  # Lança exceção para status HTTP de erro
                data = response.json()
                success = True  # Se chegou aqui, a requisição foi bem-sucedida
            except requests.RequestException as e:
                attempt += 1
                print(f"Tentativa {attempt}/3 falhou para página {page}: {e}")
                time.sleep(2)  # Aguarda 2 segundos antes de tentar novamente
                if attempt == 3:
                    raise RuntimeError(f"Erro após 3 tentativas ao buscar dados da página {page}") from e

        # Se não houver mais dados na API, interrompe o loop
        if not data:
            break

        all_data.extend(data)
        page += 1

    # Cria uma SparkSession para processar os dados como DataFrame distribuído
    spark = SparkSession.builder.appName("MageDataLoad").getOrCreate()
    df_spark = spark.createDataFrame(all_data)

    # Converte o DataFrame Spark para Pandas, mais compatível com Mage.ai
    df_pandas = df_spark.toPandas()

    spark.stop()  # Libera os recursos da SparkSession
    return df_pandas

# Função de teste que valida se o DataFrame resultante tem ao menos uma linha
@test
def test_row_count(df, *args) -> None:
    assert len(df.index) >= 1, 'Verificar se os dados possuem linhas suficientes'