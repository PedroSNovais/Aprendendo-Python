print(f'{" Desafio 82 ":=^40}')
lista = []
lpar = []
limpar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = input('Quer continuar ? [S/N] ')
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Os números digitados foram {lista}')
for i in lista:
    if i % 2 == 0:
        lpar.append(i)
    else:
        limpar.append(i)
print(f'Os números pares da lista são {lpar}')
print(f'Os números impares da lista são {limpar}')
