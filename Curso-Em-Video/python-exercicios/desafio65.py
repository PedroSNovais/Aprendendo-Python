print(f'{"Desafio 65":=^30}')
parar = False
maior = menor = cont = soma = 0
while not parar:
    num = float(input('Digite um numero: '))
    soma = soma + num
    if cont == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    parar = str(input('Deseja parar ? ')).strip().upper()[0]
    if parar != 'S':
        parar = False
    cont = cont + 1
media = soma/cont
print('Fim')
print(f'O MAIOR valor é {maior}')
print(f'O MENOR valor é {menor}')
print(f'A MÉDIA é {media}')
