import os # manipular arquivos e pastas
import glob # listar arquivos
import pandas as pd
from typing import List


def extrair_excel(path: str) -> List[pd.DataFrame]:
    """
    Lê todos os arquivos Excel (.xlsx) de uma pasta e retorna uma lista de DataFrames.

    Args:
        path (str): Caminho da pasta contendo os arquivos Excel.

    Returns:
        List[pd.DataFrame]: Lista de DataFrames com o conteúdo dos arquivos lidos.
    """
    # Lista todos os arquivos .xlsx no caminho informado
    arquivos = glob.glob(os.path.join(path, "*.xlsx"))

    lista_data_frame = []  # Lista que armazenará os DataFrames

    # Itera sobre os arquivos encontrados e carrega cada um como DataFrame
    for file in arquivos:
        data = pd.read_excel(file)
        lista_data_frame.append(data)

    # Retorna a lista de DataFrames
    return lista_data_frame


if __name__ == "__main__":
    lista_data_frame = extrair_excel(path="data/input")
    print(lista_data_frame)