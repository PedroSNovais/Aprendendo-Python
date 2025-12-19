# 05 faça um programa que leia um numero e mostre o seu sucessor e antecessor
print('{:=^30}'.format('Desafio 05'))
n = int(input('digite oum numero:'))
at = n - 1
sc = n + 1
print('O antecessor de {} é {} e o seu sucessor é {}'.format(n, at, sc))

# 06 crie um algoritimo que leia um numero e mostre o seu dobro triplo e raiz quadrada
print('{:=^30}'.format('Desafio 06'))

n = int(input('Digite um numero:'))

print(' O dobro de {} é {}.\n O triplo de {} é {}.\n A raiz quadrada de {} é {:.2f}.'.format(n, n+n, n, n*3, n, n**(1/2)))

# 07 crie um programa que leia as notas de um aluno e de a media aritimetica
print('{:=^30}'.format('Desafio 08'))
n1 = float(input('insira a nota do aluno:'))
n2 = float(input('insira a segunda nota:'))
m = (n1 + n2)/2
print('a media das notas do aluno é igual a {}'.format(m))