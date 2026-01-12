import moeda
num = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, formato=True)}')
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, formato=True)}')
print(f'{moeda.moeda(num)} com o aumento de 10% é {moeda.aumentar(num, 10, formato=True)}')
print (f'{moeda.moeda(num)} com a diminuição de 15% é {(moeda.diminuir(num, 15, formato=True))}')
