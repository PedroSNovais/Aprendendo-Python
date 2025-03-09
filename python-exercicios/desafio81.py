print(f'{" Desafio 81 ":=^40}')
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar ? [S/N] ')).strip().lower()[0]
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(lista)} Números')
print(f'A lista em ordem decrescente é {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 está na lista nas posições ', end='')
    for p, v in enumerate(lista):
        if v == 5 :
            print(p, '...', end='')
else:
    print('\nO número 5 não está na lista...')
