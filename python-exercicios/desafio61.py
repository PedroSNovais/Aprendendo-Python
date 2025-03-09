print(f'{"Desafio 61":=^30}')
n = int(input('Digite o primeiro termo de uma P.A:'))
r = int(input('Digite o valor da RAZÃO:'))
c = 1
while c < 11:
    print(f'O {c}º termo da sua P.A é {n}')
    n = n + r
    c += 1
print('Fim')
