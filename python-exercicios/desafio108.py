import moeda
num = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'{moeda.moeda(num)} com o aumento de 10% é {moeda.moeda(moeda.aumentar(num))}')
print (f'{moeda.moeda(num)} com a diminuição de 15% é {moeda.moeda((moeda.diminuir(num)))}')
