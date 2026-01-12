print(f'{"Desafio 51":=^30}')
n = int(input('Digite o valor do primeiro termo da P.A: '))
r = int(input('Digite o valor da RAZÃO da P.A: '))
print(f'o primeiro termo da sua P.A é {n}')
for c in range(0, 9):
    n = n + r
    print(f'O proximo termo da sua P.A é {n}')
