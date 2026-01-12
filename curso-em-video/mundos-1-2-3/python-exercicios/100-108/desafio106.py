from teste import titulo


def txtlinha(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


def cor(cod=''):
    print(f'\033[{cod}m')


# programa principal
titulo('Desafio 106')
while True:
    cor('42')
    txtlinha('Mini-Sistema de ajuda PyHelp')
    cor()
    cor('31')
    print('Digite "FIM" para finalizar o programa !!!')
    codigo = input('Digite um codigo Python para ver seu Docstring: ')
    cor()
    if codigo == 'FIM':
        cor('41;30')
        txtlinha('<<<  O PROGRAMA FOI FINALIZADO >>>')
        break
    cor('7;40')
    help(codigo)
    cor()
