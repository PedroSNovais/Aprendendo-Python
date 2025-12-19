
print(f'\033[1;30;41m{"Desafio 01":=^30}\033[m')
nome = input('qual seu nome ? ').strip()
nome = nome.title()
print(f'É um prazer te conhecer \033[4;34m{nome}\033[m !!!')

# ex 02
print(f'\033[1;30;41m{"Desafio 02":=^30}\033[m')
print('Digite sua data de nascimento: ')
d = str(input('DIA: '))
m = str(input('MÊS: '))
a = str(input('ANO: '))
print(f'Você nasceu no dia \033[34m{d}\033[m do mês \033[34m{m}\033[m do ano \033[34m{a}\033[m')
