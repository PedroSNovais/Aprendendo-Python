valor = float(input())

valor = valor * 100

notas = [10000, 5000, 2000, 1000, 500, 200]
print("NOTAS:")
for nota in notas:
    quantidade_nota = valor // nota
    valor = valor % nota
    print(f'{quantidade_nota:.0f} nota(s) de R$ {nota/100:.2f}')

moedas = [100, 50, 25, 10, 5, 1]
print('MOEDAS:')
for moeda in moedas:
    quantidade_moeda = valor // moeda
    valor = valor % moeda
    print(f'{quantidade_moeda:.0f} moeda(s) de R$ {moeda/100:.2f}')
