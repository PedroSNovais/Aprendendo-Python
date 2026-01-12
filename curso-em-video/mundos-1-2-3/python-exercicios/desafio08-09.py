# 08
print('{:=^30}'.format('Desafio 08'))
m = int(input('digite uma distancia em metros:'))
print(
    f'{m} metros são\n {m / 10 / 10 / 10}km\n {m / 10 / 10}hm\n {m / 10}dam\n {m * 10}dm\n '
    f'{m * 10 * 10}cm\n {m * 10 * 10 * 10}mm')

# 09 crie um programa que leia um numero e mostre a tabuada do mesmo
print('{:=^30}'.format('Desafio 09'))
n = int(input('Digite um numero para ver sua tabuada:'))
print('{:-^30}'.format('-'))
print(f'{n} X 1 = {n*1}\n{n} X 2 = {n*2}\n{n} X 3 = {n*3}\n{n} X 4 = {n*4}\n{n} X 5 = {n*5}\n{n} X 6 = {n*6} '
      f'\n{n} X 7 = {n*7}\n{n} X 8 = {n*8}\n{n} X 9 = {n*9}\n{n} X 10 = {n*10}')
print('{:-^30}'.format('-'))
