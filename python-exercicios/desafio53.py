print(f'{"Desafio 53":=^30}')
frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
print(frase, end='')
print(f' ao contrario {frase[::-1]}')
if frase == frase[::-1]:
    print('É PALINDROMO.')
else:
    print('NÃO É PALINDROMO.')

