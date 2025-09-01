print(f'{" Desafio 66 ":=^30}')
n = s = c = 0
while True:
    n = int(input('DIGITE UM NÚMERO (999 para parar ): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'FIM DO PROGRAMA !!')
print(f'VOCÊ DIGITOU {c} NÚMEROS E A SOMA É {s}')
