print(f'\033[4;30;44m{"Desafio 33":=^30}\033[m')
a = int(input('Digite um número:'))
b = int(input('Digite outro número'))
c = int(input('Digite o ultimo número'))
# para achar o menor
menor = a

if c < b and c < a:
    menor = c
if b < c and b < a:
    menor = b
# achar o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior numero é \033[42;30m{} !\033[m \nO menor numero é \033[43;30m{} !\033[m'.format(maior, menor))
