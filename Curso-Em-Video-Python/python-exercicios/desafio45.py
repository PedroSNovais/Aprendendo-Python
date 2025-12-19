from time import sleep
from random import randint

print(f'{" Desafio 45 ":=^47}')
print(f'\033[32m{" PEDRA ":*>20}\033[m\033[33m{"PAPEL"}\033[m\033[35m{" TESOURA ":*<20}\033[m')
maquina = randint(0, 2)
print('''OPÇÕES:
    [ 0 ] PEDRA     [ 1 ] PAPEL     [ 2 ] TESOURA
    ''')
jogador = int(input('\033[4;34mQUAL SUA JOGADA:\033[m '))
sleep(0.5)
print('     \033[33mJO\033[m')
sleep(0.5)
print('             \033[35mKEN\033[m')
sleep(0.5)
print('                     \033[32mPÔ!!\033[m')

itens = ('\033[32mPEDRA\033[m', '\033[33mPAPEL\033[m', '\033[35mTESOURA\033[m')

if maquina == jogador:
    print('\033[33mEMPATE\033[m')

elif jogador == 0 and maquina == 2 or maquina == 1 and jogador == 2 or maquina == 0 and jogador == 1:
    print('\033[4;32mO JOGADOR GANHOU !!!!\033[m')

elif maquina == 0 and jogador == 2 or maquina == 1 and jogador == 0 or maquina == 2 and jogador == 1:
    print('\033[4;31mO JOGADOR PERDEU !\033[m')
else:
    print(f'\033[31mOPÇÃO INVALIDA. TENTE NOVAMENTE!\033[m')
if 0 <= jogador < 3:
    print(f'A maquina esscolheu {itens[maquina]}.')
    print(f'O Jogador escolheu {itens[jogador]}.')
