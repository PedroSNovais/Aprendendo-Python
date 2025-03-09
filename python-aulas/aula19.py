print(f'{" Bibliotecas ":=^40}')
dados = {'nome': 'pedro', 'idade': 16, 'sexo': 'M'}
print(dados.values())
print(dados.keys())
print(dados.items())
dados['altura'] = 177
dados['notas'] = [10, 9.7]
dados['notas'].append(5)
print(dados['altura'])
for k, v in dados.items():
    print(f' {k} é {v}')
