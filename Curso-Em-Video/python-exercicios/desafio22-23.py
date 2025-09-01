# Desafio 22
print(f'\033[1;30;45m{"Desafio 22":=^30}\033[m')
nomec = input('Digite seu nome completo:')
nomec.strip()
print(nomec.upper())
print(nomec.lower())
nomec = nomec.split()
nomecj = ''.join(nomec)
print(f'O seu nome completo possui {len(nomecj)} letras!\n\033[4;44m(sem contar espaços)\033[m')
print(f'O seu primeiro nome é "\033[4;34m{nomec[0]}\033[m" e possui \033[30;41m{len(nomec[0])} letras\033[m!')

# Desafio 23
print('{:=^30}'.format('Desafio 23'))
num = int((input('Digite um numero de 0 a 9999:')))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'O numero que você digitou possui:')
print(f'{u} Unidades ')
print(f'{d} Dezenas')
print(f'{c} Centenas')
print(f'{m} Milhares')
