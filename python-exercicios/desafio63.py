print(f'{"Desafio 63":=^30}')
n = int(input('Digite um numero inteiro: '))
t1 = 0
t2 = 1
print(f'Abaixo segue os {n} primeiros digitos da sequencia de Fibonacci.')
while n > 0:
    print(t1, '→ ', end='')
    t1 = t1 + t2
    t2 = t1 - t2
    n = n - 1
print('ACABOU')
