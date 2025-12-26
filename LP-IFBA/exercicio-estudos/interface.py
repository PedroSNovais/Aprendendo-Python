"""
Módulo de interface do usuário para o gerenciador de tarefas no terminal.
"""

def exibir_menu():
    """
    Exibe um menu de opções para o usuário e retorna a opção selecionada.
    """
    menu_str = '''
    Opções do menu: 
    1. Cadastrar nova tarefa
    2. Listar tarefas
    3. Atualizar status da tarefa
    4. Remover tarefa
    5. exibir resumo das tarefas
    0. Sair
    '''
    print(menu_str)

def limpar_terminal():
    """
    Limpa o terminal para melhorar a legibilidade.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_tarefas(tarefas):
    """
    Exibe a lista de tarefas no terminal.
    
    Parâmetros:
    tarefas (list): Lista de dicionários representando as tarefas.
    """
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    for tarefa in tarefas:
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"ID: {tarefa['id']} | Descrição: {tarefa['descricao']} | Status: {status}")

def exibir_resumo(tarefas):
    """
    Exibe um resumo das tarefas, incluindo totais e status.
    
    Parâmetros:
    tarefas (list): Lista de dicionários representando as tarefas.
    """
    total = len(tarefas)
    concluidas = sum(1 for tarefa in tarefas if tarefa['concluida'])
    pendentes = total - concluidas
    
    print(f"Resumo das Tarefas:")
    print(f"Total de Tarefas: {total}")
    print(f"Tarefas Concluídas: {concluidas}")
    print(f"Tarefas Pendentes: {pendentes}")