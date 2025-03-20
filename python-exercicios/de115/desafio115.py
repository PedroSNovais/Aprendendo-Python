from uteis115 import *
print(f'{" Desafio 115 ":*^40}')


# recebendo dados
pessoas = list()
while True:
    p = dados()
    pessoas.append(p)
    # continuar ?
    resp = continuar()
    if resp == 'N':
        break
    else:
        print("-"*30)
arq = open('arquivo.txt', 'a')
for p in pessoas:
    n1 = list()
    for c in range(0, 2):
        n1.append(p['nome'][c])
        n1.append(' ')
    i = n1
    print(i)
    arq.writelines(i)

arq.close()
print('<<<<< Fim do Programa >>>>')
