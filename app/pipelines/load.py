import pandas as pd
import os 


def salva_excel(data_frame: pd.DataFrame, caminho_pasta: str, nome_arquivo: str) -> str:
    """
    Salva um DataFrame como arquivo Excel (.xlsx) no caminho especificado.

    Args:
        data_frame (pd.DataFrame): DataFrame a ser salvo.
        caminho_pasta (str): Caminho da pasta onde o arquivo será criado.
        nome_arquivo (str): Nome do arquivo (sem extensão).

    Returns:
        str: Mensagem de confirmação do salvamento.
    """
    # Verifica se a pasta existe; cria se não existir
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

    # Salva o DataFrame como arquivo Excel
    data_frame.to_excel(f"{caminho_pasta}/{nome_arquivo}.xlsx", index=False)

    return "Arquivo salvo com sucesso."



