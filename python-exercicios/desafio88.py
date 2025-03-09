print(f'{" Desafio 88 ":=^40}')
from random import randint
from time import sleep
palpites = []
jogo = []
print(f'{"--" * 20}\n {" PALPITES MEGA SENA ":^40}\n{"--" * 20}')
nj = int(input('Quantos jogos você quer ? '))
for c in range(0, nj):
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    palpites.append(jogo[:])
    jogo.clear()
print(f'{"-=" * 5} {"Sorteando Jogos"} {"-=" * 5}')
for n, j in enumerate(palpites):
    sleep(1)
    print(f'JOGO {n + 1}: {sorted(j)}')
print()
print('-=' * 5, 'BOA SORTE', '-=' * 5)
