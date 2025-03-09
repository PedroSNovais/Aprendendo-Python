print(f'{" Desafio 94 ":-^40}')
pessoas = list()
individuo = dict()
idades = media = 0
while True:
    individuo['nome'] = str(input('Nome: ').strip().capitalize())
    individuo['idade'] = int(input('Idade: '))
    individuo['sexo'] = str(input('Sexo: (M/F) ').strip().upper()[0])
    while individuo['sexo'] not in 'MF':
        if individuo['sexo'] not in 'MF':
            print(f'SEXO INVALIDO... Digite apenas "M" ou "F" !!')
            individuo['sexo'] = str(input('Sexo: (M/F) ').strip().upper()[0])
    resp = str(input('Quer continuar ? (S/N)').strip().upper()[0])
    while resp not in 'SN':
        if resp not in 'SN':
            print(f'RESPOSTA INVALIDO... Digite apenas "S" ou "N" !!')
            resp = str(input('Quer continuar ? (S/N) ').strip().upper()[0])
    print('-=' * 20)
    pessoas.append(individuo.copy())
    if resp == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
for p in pessoas:
    idades += p['idade']
media = idades / len(pessoas)
print(f'A média de idade foi {media:.2f} anos')
print(f'As mulheres cadastradas foram:', end=' ')
for p in pessoas:
    print(p['nome'], end=', ') if p['sexo'] == 'F' else print('', end='')
print()
print('As pessoas com idade acima da media foram:', end=' ')
for p in pessoas:
    print(p['nome'], end=', ') if p['idade'] >= media else print('', end='')
