"""
Módulo de funções para gerenciamento de tarefas.
Este módulo contém funções para criar, listar, atualizar e remover tarefas,
"""
from utils import receber_informacoes_tarefa, gerar_codigo_tarefa
from arquivo import salvar_tarefas

def criar_tarefa(lista_tarefas: list):
    try:
        tarefa = receber_informacoes_tarefa()
        tarefa["codigo"] = gerar_codigo_tarefa(tarefa, lista_tarefas)
        lista_tarefas.append(tarefa)
        salvar_tarefas(lista_tarefas)
        print("Tarefa criada com sucesso!")
        

    except ValueError as e:
        print(f"Erro ao criar tarefa: {e}")

def atualizar_status_tarefa(codigo: str, lista_tarefas: list):
    """
    Atualiza o status de uma tarefa específica na lista de tarefas.
    
    Parâmetros:
    codigo (str): O código único da tarefa a ser atualizada.
    lista_tarefas (list): A lista de tarefas onde a tarefa será atualizada."""
    
    for tarefa in lista_tarefas:
        if tarefa["codigo"] == codigo:
            tarefa["concluida"] = True if not tarefa["concluida"] else False
            tarefa["status"] = "concluida" if not tarefa["status"] == "concluida" else "pendente"
            salvar_tarefas(lista_tarefas)
            print("Status da tarefa atualizado com sucesso!")
            return
    else:
        print("Tarefa não encontrada.")

def remover_tarefa(codigo: str, lista_tarefas: list):
    """
    Remove uma tarefa específica da lista de tarefas.
    
    Parâmetros:
    codigo (str): O código único da tarefa a ser removida.
    lista_tarefas (list): A lista de tarefas onde a tarefa será removida.
    """
    for i, tarefa in enumerate(lista_tarefas):
        if tarefa["codigo"] == codigo:
            del lista_tarefas[i]
            salvar_tarefas(lista_tarefas)
            print("Tarefa removida com sucesso!")
            return
    else:
        print("Tarefa não encontrada.")

