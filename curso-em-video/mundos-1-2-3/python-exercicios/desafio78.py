print(f'{" Desadio 78 ":=^40}')
num = []
for p in range(0, 5):
    num.append(int(input(f'Digite um numero para a posição {p}... ')))
print('==' * 20)
print(num)

ordem = sorted(num)
print(f'O maior valor digitado foi \033[1;31m{ordem[4]}\033[m nas posições\033[4;36m ', end='')
for p, n in enumerate(num):
    if ordem[4] == n:
        print(p, '... ', end='')
print('\033[m')
print(f'\nO menor valor digitado foi \033[1;31m{ordem[0]}\033[m nas posições\033[4;36m ', end='')
for p, n in enumerate(num):
    if n == ordem[0]:
        print(p, '... ', end='')
print('\033[m')
