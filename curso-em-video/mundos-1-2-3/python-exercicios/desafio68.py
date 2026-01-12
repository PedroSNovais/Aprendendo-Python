from random import randint
print(f'{" Desafio 68 ":=^30}')
print(f'''{"-=" * 20}
VAMOS JOGAR \033[35mPAR\033[m OU \033[33mIMPAR\033[m ?
{"-=" * 20}''')
soma = maquina = randint(0, 10)
while True:
    pi = str(input('Qual você quer ? [P/I]: ')).strip().upper()[0]
    user = int(input('Digite o valor: '))
    soma += user
    if pi == 'P':
        j = '\033[35mJOGADOR\033[m'
        m = '\033[33mMAQUÍNA\033[m'
    else:
        m = '\033[35mMAQUÍNA\033[m'
        j = '\033[33mJOGADOR\033[m'
    print('-' * 40)
    print(f'O {j} jogou {user} e a {m} jogou {maquina}')
    print(f'A soma vale {soma} !')
    if soma % 2 == 0:
        print('É PAR')
    else:
        print('É IMPAR')
    print('-' * 40)