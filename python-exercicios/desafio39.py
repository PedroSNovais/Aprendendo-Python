import datetime
print(f'{"Desafio 39":=^30}')
sexo = str(input('qual é o seu sexo ?'))

if sexo in  ' masculino  homem ':
    user = int(input('digite o ano do seu nascimento: '))
    anoat = datetime.date.today().year
    idade = (anoat - user)
    x = 18 - idade
    print(f'\033[mVocê tem \033[31m{idade} anos.\033[m')
    if idade < 18:
        print(f'Você deverá se alistar em \033[32m{anoat + x}\033[m')
    elif idade == 18:
        print(f'\033[4;31;40mVocê deve se alistar agora mesmo\033[m !!')
    elif idade > 18:
        x = idade - 18
        print(f'Você se alistou no ano de \033[4;34m{anoat - x}\033[m')
else:
    print('você nao tem nada pra fazer aqui!')
