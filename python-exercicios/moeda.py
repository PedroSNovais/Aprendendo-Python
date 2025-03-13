print(f'{" Desafio 107 ":*^40}')


def dobro(n):
    n *= 2
    return n


def metade(n):
    t = int(n)
    t = t / 2
    return t


def aumentar(n, pc=10):
    t = int(n)
    t += (t * pc) / 100
    return t

def diminuir(n, pc=15):
    t = int(n)
    t -= (t * pc) / 100
    return t
