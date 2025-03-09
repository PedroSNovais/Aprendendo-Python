print(f'{"Desafio 35":=^30}')
a = float(input('Digite o valor de uma reta:'))
b = float(input('Digite o valor de outra reta:'))
c = float(input('Digite o valor da ultima reta:'))
if a + b > c:
    print(f'Sim, seria possivel formar um triangulo com essas retas.')
else:
    if a + c > b:
        print(f'Sim, seria possivel formar um triangulo com essas retas.')
    else:
        if b + c > a:
            print(f'Sim, é possivel formar um triangulo com essas retas.')
        else:
            print(f'Não, Não é possivel formar um triangulo com essas retas.')
