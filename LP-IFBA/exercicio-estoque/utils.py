def validar_entrada_inteira(mensagem: str, maximo: int = None, minimo: int = None):
    """
    Docstring for validar_entrada_inteira
    
    solicita e valida uma entrada de número inteiro
    
    Args: 
        mensagem (str): mensagem a ser exibida
        maximo (int, opcional): valor maximo aceito
        minimo (int, opcional): valor minimo aceito
    
    Returns: 
        int: valor inteiro validado
    """
    while True:
        try:
            valor = int(input(mensagem))

            if minimo is not None and valor < minimo:
                print("ERRO! O valor é menor que o minimo")
                continue
            
            if maximo is not None and valor > maximo:
                print("ERRO! O valor é maior que o maximo")
                continue
            return valor
        except ValueError:
            print("Erro! digite um número valido.")

def salvar_estoque(estoque: dict, nome_arquivo: str):
    """
    Salva o dicionario de estoque em um arquivo json
    
    Args:
        estoque (dict): dicionario de produtos e quantidades
        nome_arquivo (str): nome do arquivo onde o estoque sera salvo
    """
    with open(nome_arquivo, 'w') as arquivo:
        for produto, quantidade in estoque.items():
            arquivo.write(f"{produto}:{quantidade}\n")
    print("Estoque salvo com sucesso.")

def carregar_estoque(nome_arquivo: str) -> dict:
    """
    Carrega o dicionario de estoque de um arquivo json
    
    Args:
        nome_arquivo (str): nome do arquivo de onde o estoque sera carregado
    
    Returns:
        dict: dicionario de produtos e quantidades
    """
    estoque = {}
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                produto, quantidade = linha.strip().split(':')
                estoque[produto] = int(quantidade)
        print("Estoque carregado com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Iniciando com estoque vazio.")
    return estoque