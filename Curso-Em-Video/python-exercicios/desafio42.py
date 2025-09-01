print(f'{"Desafio 42":=^30}')
a = float(input('Digite um lado do triangulo:'))
b = float(input('Digite outro lado do triangulo:'))
c = float(input('Digite outro lado do triangulo'))
if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        t = 'EQUILATERO'
    elif a == b != c or a == c != b or b == c != a:
        t = 'ISÓSCELES'
    elif a != b != c != a:
        t = 'ESCALENO'
    print(f'As retas \033[32mPODEM\033[m formar um triangulo \033[4;30;46m{t}\033[m!!')
else:
    print(f'As retas \033[4;31mNÃO PODEM\033[m formar um \033[1;43mTriângulo\033[m!!')
