print(f'{" Desafio 86 ":=^40}')
l0 = []
l1 = []
l2 = []
linhas = [l0, l1, l2]
for l in linhas:
    for c in range(0, 3):
        l.append(int(input(f'Digite um número para a posição {linhas.index(l)}, {c}: ')))
print(f'{"-=" * 20}\nSua matriz é:')
print()
for l in linhas:
    print(f'({l[0]:^5}) ({l[1]:^5}) ({l[2]:^5})')
