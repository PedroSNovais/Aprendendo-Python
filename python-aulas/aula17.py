print(f'{" aula 17 ":=^30}')
lanche = ['Pizza', 'Beteraba', 'Abóbora', 'Abacate']
print(lanche)
print('=' * 30)
lanche.append('Batata')    # add o item no fim da lista
print(sorted(lanche))   # mostrando lista em ordem
print('=' * 30)
print(lanche.index('Pizza'))    # em que posição esta o item pizza
print('=' * 30)
lanche.insert(2, 'leite')   # add o item na posição desejada
print(lanche)
print('=' * 30)
# para eliminar itns da lista
lanche.remove('leite')
print(lanche)
print('--' * 30)


valores = list(range(1, 11))
print(valores)
valores = [1, 8, 3, 13, 7, 12]
print(valores)
nomes = ['eduardo', 'pedro', 'ana', 'barbara']
nomes.sort(reverse=True)
print(nomes)
print('--' * 30)


valores.append(45)
valores.append(10)
valores.insert(5, 28)
for c, v in enumerate(valores):
    print(f'Na posição {c} está o numero {v}')
