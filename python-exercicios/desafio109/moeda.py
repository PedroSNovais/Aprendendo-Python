print(f'{" Desafio 107/8 ":*^40}')


def dobro(valor, formato=False):
    valor *= 2
    if formato:
        valor = f'{valor:.2f}'
        valor = str(valor).replace('.', ',')
        valor = f'R${valor}'

    return valor


def metade(valor, formato=False):
    valor = valor / 2
    if formato:
        valor = f'{valor:.2f}'
        valor = valor.replace('.', ',')
        valor = f'R${valor}'
    return valor


def aumentar(valor, pcento=10, formato=False):
    valor += (valor * pcento) / 100
    if formato:
        valor = f'{valor:.2f}'
        valor = valor.replace('.', ',')
        valor = f'R${valor}'
    return valor

def diminuir(valor, pcento=15, formato=False):
    valor -= (valor * pcento) / 100
    if formato:
        valor = f'{valor:.2f}'
        valor = valor.replace('.', ',')
        valor = f'R${valor}'
    return valor


def moeda(msg, moeda='R$'):
    msg = f'{moeda}{msg:.2f}'.replace('.', ',')
    return msg

