def dados():
   while True:
        try:
            nome = str(input('Nome: ').strip().capitalize()).split()
            snome = str(input('Sobrenome: ').strip().capitalize()).split()
            idade = int(input('Idade: '))
            return {'nome': nome, 'idade': idade, 'snome': snome}

        except (TypeError, ValueError):
            print('\033[1;31mErro! Digite dados validos...\033[m')


def continuar():
    while True:
        r = str(input('Quer continuar ? [S/N] ').strip().capitalize()[0])
        if r in 'SN':
            return r
        else:
            print('\033[1;31mErro! Digite "Sim" ou "Não"...\033[m')
