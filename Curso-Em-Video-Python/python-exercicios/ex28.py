from random import randint
print(f'{"Desafio 28":=^30}')
print(f'\033[1;30;41m{"JOGO DE ADIVINHAÇÃO":^40}\033[m')
print(f'A maquina sorteou um numero de 0 a 5!')
n = randint(0, 5)
nj = int(input('qual foi o numero sorteado pela maquina: '))
if n == nj:
    print(f'\033[1;30;42mVocê ganhou o jogo!\033[m \nO número sorteado foi realmente \033[4;32m{nj}\033[m')
else:
    print(f'\033[1;30;41mVocê perdeu !!!!!!\033[m \nVocê escolheu {nj} e o numero certo era {n}')
