print(f'{" Desafio 59 ":=^60}')
n1 = float(input('Digite um Número: '))
n2 = float(input('Digite outro Número: '))
sair = False
while not sair:

    print('''
    SUAS OPÇÕES:
    ----------------------------------------------------
    [ 1 ] SOMAR     [ 2 ] MULTIPLICAR   [ 3 ] QUAL MAIOR
    
    [ 4 ] NUMEROS NOVOS     [ 5 ] SAIR DO PROGRAMA 
    -----------------------------------------------------''')
    print('\033[36m=======================================================\033[m')
    opera = int(input('ESCOLHA UMA OPÇÃO: '))
    if opera == 1:
        soma = n1 + n2
        print(f'A SOMA dos numeros resulta em {soma}')
    elif opera == 2:
        prod = n1 * n2
        print(f'A Multiplicação dos numeros resulta em {prod}')
    elif opera == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O MAIOR VALOR é {maior}')
    elif opera == 4:
        n1 = float(input('DIGITE UM NÚMERO: '))
        n2 = float(input('DIGITE OUTRO NÚMERO: '))
    elif opera == 5:
        sair = True
    else:
        print(f'OPÇÃO INVALIDA. TENTE OUTRA!')
    print('\033[36m=========================================================\033[m')
print('\033[31mFINALIZANDO...\033[m')
print('FIM DO PROGRAMA. VOLTE SEMPRE!!')
