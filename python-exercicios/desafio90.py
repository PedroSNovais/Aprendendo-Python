print(f'{" Desafio 90 ":-^40}')
aluno = dict()
aluno["Nome"] = str(input(f'NOME: ').strip().capitalize())
aluno['Média'] = float(input(f'MÉDIA: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-=' * 20)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
