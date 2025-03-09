from time import sleep
from random import randint
print(f'{" Desafio 58 ":=^46}')
print(f'\033[33m{"*":*<13}\033[m{" JOGO de ADIVINHAÇÃO "}\033[33m{"*":*>13}\033[m')
print(' VOU PENSAR EM UM \033[35mNUMERO DE 0 A 10\033[m!!!')
sleep(0.5)
print(' PROCESSANDO...')
jogo = randint(0, 10)
sleep(2)
palpite = 20
cont = 0
while palpite != jogo:
    cont = cont + 1
    palpite = int(input('   TENTE ADIVINHAR QUAL NUMERO EU PENSEI: '))
    if palpite != jogo:
        print(f'    \033[31mERROU!!!!!\033[m')
        if palpite < jogo:
            print('    \033[36mTENTE MAIS \033[33mALTO...\033[m')
        else:
            print('    \033[36mTENTE MAIS \033[35mBAIXO...\033[m')
    else:
        sleep(0.5)
        print('')
        print(f'    \033[32mCERTA A RESPOSTA !!\033[m')
        print('')
        sleep(1)
print(f' VOCÊ PRECISOU DE \033[33m{cont} TENTATIVAS\033[m PARA ACERTAR !!!')
print(f' O NÚMERO ESCOLHIDO POR MIM FOI \033[35m{jogo}\033[m')
