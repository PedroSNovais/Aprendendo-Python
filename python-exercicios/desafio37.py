print(f'{"Desafio 37":=^30}')
numero = int(input('Digite um numero inteiro qualquer:'))
print('[ 1 ] para Binario\n[ 2 ] para Octal\n[ 3 ] para Hexadecimal.')
base = int(input('\033[4;33;40mDigite o codigo da base que você deseja usar:\033[m'))
if base == 1:
    num = bin(numero)
    base = 'Binario'
elif base == 2:
    num = oct(numero)
    base = 'Octal'
elif base == 3:
    num = hex(numero)
    base = 'Hexadecimal'
else:
    print('Opção invalida. Tente novamente.')
print(f'O numero {numero} em {base} se torna {num [2:]}!')
