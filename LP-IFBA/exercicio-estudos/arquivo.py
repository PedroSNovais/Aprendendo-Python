"""
Módulo responsavel pela percistencia dos dados.
salva e carregue os dados em arquivos.
"""

import os
import json

NOME_ARQUIVO = "tarefas.json"

def definir_caminho_arquivo() -> str:
    """
    Define o caminho completo do arquivo de tarefas.

    Returns:
        str: O caminho completo do arquivo de tarefas.
    """
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(diretorio_atual, NOME_ARQUIVO)

def salvar_tarefas(lista_de_tarefas: list) -> None:
    """
    Salva a lista de tarefas em um arquivo JSON.

    Args:
        lista_de_tarefas (list): A lista de tarefas a ser salva.
    """
    caminho_arquivo = definir_caminho_arquivo()
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_de_tarefas, arquivo, ensure_ascii=False, indent=4)


def carregar_tarefas() -> list:
    """
    Carrega a lista de tarefas de um arquivo JSON.

    Returns:
        list: A lista de tarefas carregada do arquivo. Retorna uma lista vazia se o arquivo não existir.
    """
    caminho_arquivo = definir_caminho_arquivo()
    if not os.path.exists(caminho_arquivo):
        return []
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)
