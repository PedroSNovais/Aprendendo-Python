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