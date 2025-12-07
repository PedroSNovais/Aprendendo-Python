def adicionar_produto(estoque: dict):
    """
    Adiciona um produto como key no dicionario
    Args: 
        estoque (dict): dicionario de produtos e quantidades
    
    """
    nome = str(input("Digite o nome do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))    
    produto = {nome: quantidade}
    estoque.update(produto)
    return 0 

def atualizar_quantidade():
    """
    Atualiza o valor referente a key do produto

    """
    return 0
def remover_produto():
    """
    Remove um produto do dicionario

    """
    return 0
def verificar_quantidade():
    """
    Verifica a quantidade de um produto específico
    """
    return 0