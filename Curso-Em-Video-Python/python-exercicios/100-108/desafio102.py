from teste import titulo


def fatorial(num, show=True):
    """
     -> mostra o fatorial de um numero
    :param num: número a ser calculado
    :param show: (opcional) mostrar o calculo
    :return: fatorial do numero
    feito por PedroSNovais
    """
    if show:
        print(num, end='x')
    for fat in range(num - 1, 0, -1):
        num *= fat
        if show:
            print(fat, end='x')
    if show:
        print('0 = ', end='')
    print(num)


titulo('Desafio 102')
fatorial(5, True)
print('-=' * 20)
help(fatorial)
