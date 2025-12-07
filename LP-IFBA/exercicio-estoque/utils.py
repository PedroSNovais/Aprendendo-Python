def validar_entrada_inteira(mensagem:str, maximo:int = None, minimo:int = None ):
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
        except ValueError():
            print("Erro! digite um número valido.")