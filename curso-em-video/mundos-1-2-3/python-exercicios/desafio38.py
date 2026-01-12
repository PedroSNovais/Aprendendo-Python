print(f'{"Desafio 38":=^30}')
n1 = float(input('Digite um numero para ser comparado: '))
n2 = float(input('Digite outro numero para ser comparado: '))
if n1 < n2:
    print(f'{n2} é maior do que {n1}!')
elif n2 < n1:
    print(f'{n1} é maior que {n2}!')
else:
    print('Os numeros são  iguais!')
