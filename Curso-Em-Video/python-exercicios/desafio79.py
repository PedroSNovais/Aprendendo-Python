print(f'{" Desafio 79 ":=^40}')
numeros = []
continuar = 's'
while True:
    if continuar == 'n':
        break
    n = (int(input('Digite um valor: ')))
    if n in numeros:
        print('Esse número já está na lista !')
    else:
        numeros.append(n)
    continuar = input('Quer continuar ? [S/N]').strip().lower()[0]
    while True:
        if continuar in 'sn':
            break
        continuar = input('Quer continuar ? ').strip().lower()[0]
numeros.sort()
print(f'A lista com os numeros unicos é, em ordem cresente, {numeros}')
