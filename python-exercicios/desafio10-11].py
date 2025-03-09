# 10 faça um programa que leia um valor em reais e converta em dolares
print('{:=^30}'.format('Desafio 10'))
r = float((input('quantos reais você tem na carteira ?')))
print(f'Com {r} reais você compra {r / 6.16:.2f} dolares')
# 11 faça um programa que leia quantos metros tem uma parede e de a quantidade de tinta nessesaria para pinta-la
print('{:=^30}'.format('Desafiio 11'))
al = float(input('Quantos metros de Altura da parede que você quer pintar ? '))
c = float(input('E de comprimento ?'))
a = al*c
print(f'sua parede de {al}X{c} tem a area de {a}m2')
print('com uma tinta que rende 2 metros por litro.\n'
      'você precisaria de {} litros de tinta para pintar essa parede.'.format(a/2))
