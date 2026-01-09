valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
print("NOTAS:")
for nota in notas:
    quantidade_nota = valor // nota
    valor = valor % nota
    print(f'{quantidade_nota:.0f} nota(s) de R$ {nota:.2f}')

moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print('MOEDAS:')
for moeda in moedas:
    quantidade_moeda = valor // moeda
    valor = valor % moeda
    print(f'{quantidade_moeda:.0f} moeda(s) de R$ {moeda:.2f}')
