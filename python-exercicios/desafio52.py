print(f'{"Desafio 52":=^30}')
num = int(input('Digite um número: '))
cont = 0
contador = 0
for c in range(0, num):
    cont += 1
    d = num % cont
    if d == 0:
        print('\033[33m', end='')
        contador += 1
    else:
        print('\033[31m', end='')
    print(d, end=' ')
print('\033[m')
print(f'{num} é divisivel por {contador} numeros!')
if contador > 2:
    print(f'{num} NÃO É PRIMO')
else:
    print(f'{num} É PRIMO')

