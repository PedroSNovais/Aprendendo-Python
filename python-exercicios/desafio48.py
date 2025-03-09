print(f'{"Desaffio 48":=^30}')
s = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:  # vendo se o numero é impar e divide por 3
        contador = contador + 1
        s = s + c
print(f' A somatoria dos {contador} numeros é \033[34m{s}\033[m !')
print('FIM')
