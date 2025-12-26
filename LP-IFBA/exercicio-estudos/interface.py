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
