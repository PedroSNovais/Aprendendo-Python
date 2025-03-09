print(f'{"Desafio 50":=^30}')
s = 0
n = 0
for c in range(1, 7):
    if n % 2 == 0:
        s = s + n
    n = int(input('Digite um numero:'))
s = s + n
print(f'A SOMA dos numeros PARES que você digitou é \033[35m{s}\033[m')
