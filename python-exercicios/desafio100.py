from random import randint
from time import sleep


def sortear(lista):
    print('SORTEANDO 5 VALORES...')
    for c in range(0, 5):
        sleep(0.5)
        lista.append(randint(0, 10))
        print(lista[c], end=' ')
    print('Pronto!')


def somapar(lista):
    soma = 0
    for n, i in enumerate(lista):
        if i % 2 == 0:
            soma += i
    print(f'A soma dos pares de {lista} é {soma}')


print(f'\033[1;36m{" Desafio 100 ":*^40}\033[m')
num = list()
sortear(num)
somapar(num)
print("-=" * 20)
