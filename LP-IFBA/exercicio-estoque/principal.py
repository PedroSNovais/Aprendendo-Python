from utils import validar_entrada_inteira

def adicionar_produto(estoque: dict):
    """
    Adiciona um produto como key no dicionario
    Args: 
        estoque (dict): dicionario de produtos e quantidades
    
    """
    nome = str(input("Digite o nome do produto: "))
    quantidade = validar_entrada_inteira("Digite a quantidade do produto: ")    
    produto = {nome: quantidade}
    estoque.update(produto)
    return 0 

def atualizar_quantidade(estoque: dict):
    """
    Atualiza o valor referente a key do produto
    Args: 
        estoque (dict): dicionario de produtos e quantidades
    """
    produto = str(input("Digite o nome do produto que deseja atualizar: "))
    if produto in estoque:  
        nova_quantidade = validar_entrada_inteira("Digite a nova quantidade do produto: ")
        estoque[produto] = nova_quantidade
    else:
        print("Produto não encontrado no estoque.")
    return 0

def remover_produto(estoque: dict):
    """
    Remove um produto do dicionario
    Args: 
        estoque (dict): dicionario de produtos e quantidades
    """
    produto = str(input("Digite o nome do produto que deseja remover: "))
    if produto in estoque:  
        del estoque[produto]
    else:
        print("Produto não encontrado no estoque.")
    return 0

def verificar_quantidade(estoque: dict):
    """
    Verifica a quantidade de um produto específico
    Args: 
        estoque (dict): dicionario de produtos e quantidades
    """
    produto = str(input("Digite o nome do produto que deseja verificar: "))
    if produto in estoque:
        print(f"A quantidade de {produto} no estoque é: {estoque[produto]}")
    else:
        print("Produto não encontrado no estoque.")
    return 0