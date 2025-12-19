print(f'{"Desafio 64":=^30}')
soma = num = 0
cont = -1
print('999 para finalizar!')
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um numero inteiro: '))
print(f'VOCÊ DIGITOU {cont} NÚMEROS!')
print(f'A soma dos Números que vc digitou é {soma} !')
