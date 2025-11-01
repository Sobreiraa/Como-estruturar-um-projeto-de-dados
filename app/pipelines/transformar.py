import pandas as pd
from typing import List


def concatenar_data_frames(lista_data_frames: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de dataframes em um único dataframe

    arg:
        lista_data_frames: lista de data_frames 

    return:
        data_frame_unico (pd.DataFrame): dataframe unico, que foi concatenado
    """
    # Pega a lista de Data Frames e concatena em um só.
    data_frame_unico = pd.concat(lista_data_frames, ignore_index=True)
    return data_frame_unico

