def dados():
   while True:
        try:
            nome = str(input('Nome: ').strip().capitalize())
            idade = int(input('Idade: '))
            return {'nome': nome, 'idade': idade}

        except (TypeError, ValueError):
            print('\033[1;31mErro! Digite dados validos...\033[m')


def continuar():
    try:
        while True:
            r = int(input('\033[1;33mSua Opção: \033[m'))
            if r in (1, 2, 3):
                return r
            else:
                print('\033[1;31mErro! Digite um número valido...\033[m')
    except Exception:
        print('\033[1;31mErro! Digite um valor valido...\033[m')


def titulo(msg="MENU PRINCIPAL"):
    print('-' * 40)
    print(f'{msg:^40}')
    print('-' * 40)
