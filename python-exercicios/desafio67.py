print(f'{" DESAFIO 67 ":=^30}')
print('DIGITE UM VALOR NEGATIVO PARA ENCERRAR O PROGRAMA!')
while True:
    n = int(input('DIGITE UM NUMERO PARA VER SUA TABUADA: '))
    print(f'-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:2} = {n * c}')
    print(f'-' * 30)
print('PROGRAMA FINALIZADO. Volte Sempre!')
