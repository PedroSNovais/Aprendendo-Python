print(f'{" Desafio 107/8 ":*^40}')


def dobro(n):
    t = n
    t *= 2
    return t


def metade(n):
    t = n
    t = t / 2
    return t


def aumentar(n, pc=10):
    t = n
    t += (t * pc) / 100
    return t

def diminuir(n, pc=15):
    t = n
    t -= (t * pc) / 100
    return t


# desafio 108
def moeda(msg):
    msg = int(msg)
    msg = f'R${msg}.00'
    return msg
