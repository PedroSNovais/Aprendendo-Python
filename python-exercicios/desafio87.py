print(f'{" Desafio 87 ":=^40}')
somapar = soma3 = maior = 0
linhas = [[], [], []]
for l in linhas:
    for c in range(0, 3):
        l.append(int(input(f'Digite um numero para a posição {linhas.index(l)}, {c}: ')))
print('-=' * 20)
print('Sua matrix é:')
for l in linhas:
    print(f'({l[0]:^5}) ({l[1]:^5}) ({l[2]:^5})')
print('-=' * 20)
for l in linhas:
    for c in range(0, 3):
        if l[c] % 2 == 0:
            somapar += l[c]
print(f'A soma dos valores pares é {somapar}')
print(f'A soma de todos os numeros da 3º coluna é {linhas[0][2] + linhas[1][2] + linhas[2][2]}')
print(f'O maior valor da segunda linha é {max(linhas[1])}')
