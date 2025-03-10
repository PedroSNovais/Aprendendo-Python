from time import sleep


def contador(inicio, fim, passo):
    if fim < inicio:
        passo = -passo
    for c in range(inicio, fim + 1, passo):
        print(c, end=' ')
        sleep(0.5)
    print('Acabou!')
    print('-=' * 20)


print(f'{" Desafio 98 ":-^40}')
print('contagem de 1 até 10 de 1 em 1 ')
contador(1, 10, 1)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, 2)
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
if p == 0:
    p = 1
if f <= 0:
    f -= 2
print('-=' * 20)
print(f'Contagem de {i} até {f} de {p} em {p}')
contador(i, f, p)
