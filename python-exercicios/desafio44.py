print(f'{"Desafio 44":=^50}')
print(f'{" LOJAS LOCAS ":*^50}')
valor = float(input('Qual o valor do produto ? R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] À Vista Dinheiro / PIX
[ 2 ] À Vista Cartão
[ 3 ] 2x No Cartão
[ 4 ] 3x ou mais no Cartão''')
fp = int(input('Qual a forma de pagamento: '))
if fp == 1:
    desc = valor * 10 / 100
    print(f'A sua compra de R${valor:.2f} no Dinheiro ou PIX fica no valor de R${valor - desc:.2f}')
elif fp == 2:
    desc = valor * 5 / 100
    print(f'sua compra de R${valor:.2f} À Vista no Cartão fica no valor de R${valor - desc:.2f}')
elif fp == 3:
    desc = 0
    print(f'A parcela da sua compra fica 2x de R${valor / 2:.2f}')
    print(f'Ao fim você paga {valor:.2f} ')
elif fp == 4:
    parcela = int(input('serão quantas parccelas? '))
    desc = valor * 20 / 100
    valor2 = valor + desc
    print(f'A parcala da sua compra fica {parcela:.2f}x de R${valor2 / parcela:.2f}')
    print(f'Ao fim você paga {valor2:.2f}')
else:
    print(f'\033[4;31mOpção De Pagamento Invalida.\033[m \nTENTE NOVAMENTE')
