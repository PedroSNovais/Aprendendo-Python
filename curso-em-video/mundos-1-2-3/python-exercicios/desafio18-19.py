# Desafio 18
import math

print('\033[4;42;30m{:=^30}\033[m'.format('Desafio 18'))
n = float(input('digite um valor para saber seu seno e cosseno:'))
print(f'O seno de {n} é {math.sin(math.radians(n)):.2f}')
print(f'O cosseno de {n} é {math.cos(math.radians(n)):.2f}')
print(f'A tangente de {n} é {math.tan(math.radians(n)):.2f}')

# desafio 19
from random import choice
print('\033[1;30;46m{:=^30}\033[m'.format('Desadio 19'))
a1 = input('Digite o nome de um aluno:')
a2 = input('Digite o nome de outro aluno:')
a3 = input('Digite o nome de outro aluno:')
a4 = input('Digite o nome do ultimo aluno:')
A = choice([a1, a2, a3, a4])
print(f'O aluno escolhido foi\033[1;30;45m {A} \033[m!!')