print(f'{" Desafio 85 ":=^40}')
num = [[], []]
for c in range(0, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print('-=' * 20)
print(f'Os numeros pares são {sorted(num[0])}.\nOs numeros impares são {sorted(num[1])}')
