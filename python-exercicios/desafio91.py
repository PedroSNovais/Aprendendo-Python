from random import randint
from time import sleep
print(f'{" Desafio 91 ":-^40}')
jogadores = {}
for c in range(0, 4):
    nome = str(input("NOME DO JOGADOR: ").strip().upper())
    jogadores[nome] = int(randint(1, 6))
    print(f'O DADO ESTÁ ROLANDO PARA {nome}', end='')
    for pontos in range(0, 3):
        sleep(0.7)
        print(f'.', end='')
    print()
    print(f'{nome} tirou {jogadores[nome]}')
    print('-=' * 20)
print('-' * 40)
print('<<< RANKING DOS JOGADORES >>>')
for v in sorted(jogadores.values(), reverse=True):
    for j, dado in jogadores.items():
        if dado == v:
            print(f'{j:.<20}{v:>2}')
            del jogadores[j]
            break
print('<<< Fim do Programa. >>>')
