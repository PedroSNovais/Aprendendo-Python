print(f'{" Desafio 107/8/9/10 ":*^40}')


def dobro(valor, formato=False):
    valor *= 2
    return valor if not formato else moeda(valor)


def metade(valor, formato=False):
    valor = valor / 2
    return valor if not formato else moeda(valor)


def aumentar(valor, pcento=10, formato=False):
    valor += (valor * pcento) / 100
    return valor if not formato else moeda(valor)


def diminuir(valor, pcento=15, formato=False):
    valor -= (valor * pcento) / 100
    return valor if not formato else moeda(valor)


def moeda(msg, mda='R$'):
    msg = f'{mda}{msg:.2f}'.replace('.', ',')
    return msg


def resumo(valor, aumento=10, diminui=15):
    print('--' * 20)
    print(f'{"Resumo do valor":^40}')
    print('--' * 20)
    print(f'VALOR ANALISADO: {moeda(valor)}')
    print(f'DOBRO: {dobro(valor, formato=True)}')
    print(f'METADE: {metade(valor, True)}')
    print(f'AUMENTO ({aumento}%): {aumentar(valor, aumento, True)}')
    print(f'DIMINUIÇÃO ({diminui}%): {diminuir(valor, diminui, True)}')
    print('--' * 20)

