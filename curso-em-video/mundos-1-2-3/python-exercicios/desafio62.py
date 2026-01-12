print(f'{"Desafio 62":=^30}')
n = int(input('Digite o primeiro termo da sua P.A: '))
r = float(input('Digite a RAZÃO da sua P.A: '))
termos = 10
c = 1
while termos > 0:
    print(f'O {c}º termo da sua P.A é {n}')
    n = n + r
    c = c + 1
    termos -= 1
    if termos == 0:
        termos = int(input('Deseja ver quantos \033[34mtermos\033[m a mais ? '))
print('FIM DO PROGRAMA.')
