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
    
