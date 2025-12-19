# para chamar o interactive help do comando 'print' use:
""" help(print) """


def somar(a, b, c):
    # Criando Docstrings para a função "somar()"
    """
     -> soma três números
    :param a: 1º número
    :param b: 2º número
    :param c: 3º número
    :return: não tem retorno
    feito por PedroSNovais
    """
    s = a + b + c
    print(s)


somar(1, 9, 5)
help(somar)     # visualisando a docstring da minha função


# para criar parametros opcionais, torne o parametro = a algum valor quando declarar a variavel
""" def somar(a=0 b=0 c=0) """
# o programa usará o valor definido na criação caso o usuario nao digite-o
