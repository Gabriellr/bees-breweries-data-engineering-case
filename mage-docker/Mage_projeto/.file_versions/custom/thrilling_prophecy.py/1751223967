from mage_ai.io.file import FileIO
from pandas import DataFrame
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Exporta o DataFrame para um arquivo CSV dentro do diretório do projeto Mage AI.

    Exemplo de caminho: <projeto_mage>/data/bronze/breweries_raw.csv
    """
    # Caminho relativo ao diretório do projeto
    dir_path = 'data/csv'
    os.makedirs(dir_path, exist_ok=True)  # Cria o diretório, se não existir

    filepath = os.path.join(dir_path, 'breweries_raw.csv')
    FileIO().export(df, filepath)