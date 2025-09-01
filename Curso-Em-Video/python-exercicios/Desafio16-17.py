# Desafio 016
print('{:=^30}'.format('\033[4;30;41mDesafio 016\033[m'))
import math

v = float(input('Digite um numero quebrado:'))
inte = math.fabs(v)
print(f'A parte inteira de {v} é {int(inte)}')

# Desafio 017
print('\033[1;45;30m {:=^30} \033[m'.format('Desafio 017'))
cop = float(input('qual o valor do cateto oposto ?'))
cad = float(input('qual o valor do cateto adjacente ?'))
hip = (cop ** 2) + (cad ** 2)
hip2 = math.sqrt(hip)
print(f'o valor da hipotenisa é {hip2:.2f}.')
