def receber_inteiro_valido(mensagem: str, maximo: int = None, minimo: int = None) -> int:
    """
    Solicita ao usuário que insira um número inteiro válido, com opções de limites máximo e mínimo.

    Args:
        mensagem (str): A mensagem a ser exibida ao solicitar a entrada do usuário.
        maximo (int, optional): O valor máximo permitido. Se None, não há limite superior. Padrão é None.
        minimo (int, optional): O valor mínimo permitido. Se None, não há limite inferior. Padrão é None.

    Returns:
        int: O número inteiro válido inserido pelo usuário.
    """
    while True:
        entrada = input(mensagem)
        try:
            valor = int(entrada)
            if (maximo is not None and valor > maximo):
                print(f"Erro: O valor deve ser menor ou igual a {maximo}.")
                continue
            if (minimo is not None and valor < minimo):
                print(f"Erro: O valor deve ser maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Erro: Por favor, insira um número inteiro válido.")

def exibir_menu():
    """
    Exibe um menu de opções para o usuário e retorna a opção selecionada.

    Returns:
        int: A opção selecionada pelo usuário.
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

def receber_informacoes_tarefa():
    """
    Solicita ao usuário que insira informações para criar uma nova tarefa. 
    Returns:
        dict: Um dicionário contendo as informações da tarefa.
    """
    titulo = str(input("Digite o título da tarefa: "))
    descricao = str(input("Digite a descrição da tarefa: "))
    data_de_realizacao_str = str(input("Digite a data de realização da tarefa (DD/MM/AAAA): "))
    status = "pendente"
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "data_de_realizacao": data_de_realizacao_str,
        "status": status
    }
    return tarefa

def gerar_codigo_tarefa(tarefa: dict, lista_tarefas: list) -> str:
    """
    Gera um código único para a tarefa com base no timestamp atual.

    Returns:
        str: O código gerado para a tarefa.
    """
    codigo = hash(tarefa["titulo"] + tarefa["data_de_realizacao"])
    if codigo in [t["codigo"] for t in lista_tarefas]:
        print("AVISO: existe outra tarefa com o mesmo titulo e data de realização.")
        codigo += 1  # Simples ajuste para evitar colisão
    return codigo