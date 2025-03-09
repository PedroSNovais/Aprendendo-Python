print(f'{" Desafio 89 ":=^40}')
turma = []
aluno = list()
dados = list()
media = n = 0
print(f'--' * 20, f'\n{"CADASTRO DE NOTAS DE ALUNOS":^40}\n', '--' * 20)
while True:
    dados.append(str(input('NOME: ')).strip().capitalize())
    aluno.append(dados[:])
    dados.clear()
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    media = (dados[0] + dados[1]) / 2
    dados.append(media)
    aluno.append(dados[:])
    dados.clear()
    turma.append(aluno[:])
    aluno.clear()
    continuar = str(input('Quer continuar ? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print('-=' * 20)
print(f'{"Nº":<4} {"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for n, a in enumerate(turma):
    print(f'{n:<4} {a[0][0]:<10}{a[1][2]:>8.1f}')
print('-' * 26)
while True:
    n = int(input('Digite o Nº do aluno para ver as Notas: (999 para encerrar) '))
    if n == 999:
        break
    elif n >= len(turma):
        print(f'O aluno com o Nº {n} não esta cadastrado...')
        print('--' * 30)
    else:
        print(f'{"NOME:":<15} {"Nota 1:":<13} {"Nota 2:":>5}')
        print(f'{turma[n][0][0]:<15} { turma[n][1][0]:<13} {turma[n][1][1]:>5}')
        print('--' * 30)
print('--' * 30)
print('<<< FIM DO PROGRAMA >>>')
