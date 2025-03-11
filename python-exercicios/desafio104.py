from teste import titulo


def leiaint(msg):
    while True:
        n = (input(msg))
        if n.isnumeric():
            break
        else:
            print('\033[1;31m ERRO!! Digite apenas números:\033[m')
    return n

titulo('Desafio 104')
n = leiaint('Digite um número: ')
print(f'\033[4;36mVocê acabou de digitar o número\033[1;33m {n}.\033[m')
