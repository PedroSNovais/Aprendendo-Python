print(f'{"Desafio 47":=^30}')
print(f'Os numeros pares de 1 a 50 são: ')
for c in range(2, 51, 2):
    if c % 2 == 0:
        print(c, end=' ')
print('FIM')