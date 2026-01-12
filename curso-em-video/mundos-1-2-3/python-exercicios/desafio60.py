print(f'{"Desafio 60":=^30}')
num = int(input('Digite um numero para ver ser fatorial: '))
fatorial = num

# usando for
'''for fator in range(num - 1, 0, -1):
    fatorial = fatorial * fator'''

#usando while
fator = num - 1
while fator != 0:
    fatorial = fatorial * fator
    fator = fator - 1


print(f'O FATORIAL de {num} é {fatorial}.')
