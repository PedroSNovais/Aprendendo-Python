print(f'{" Desafio 84 ":=^40}')
pessoas = []
dados = list()
cont = maior = menor = 0
while True:
    dados.append(str(input('Digite o nome da pessoa: ')).capitalize())
    dados.append(float(input('Digite o peso da pessoa: ')))
    if cont == 0:
        menor = maior = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    resp = str(input('Quer continuar ? [S/N] ')).strip().lower()[0]
    if resp not in 'SsnN':
        while True:
            resp = str(input('Quer continuar ? [S/N] ')).strip().lower()[0]
            if resp in 'SsNn':
                break
    if resp in 'Nn':
        break
print('-=' * 20)
for n, p in enumerate(pessoas):
    print(f'A {n + 1}º Pessoa, {p[0]} tem {p[1]}KG de peso.')
print('-=' * 20)
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print([p[0]], end=' ')
print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print([p[0]], end=' ')
