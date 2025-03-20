from uteis115 import *
print(f'{" Desafio 115 ":*^40}')


# recebendo dados
pessoas = list()
while True:
    p = dados()
    # transformando em lista de escritas para printar (TEM COMO SIMPLIFICAR MAS EU TENHO PREGUIÇA)
    if len(p['snome']) == 0:
        pessoas.append(f'{p["nome"][0]} {p["idade"]:>16} anos')
    else:
        pessoas.append(f'{p["nome"][0]} {p["snome"][len(p["snome"])-1]} {p["idade"]:>10} anos')
    # continuar ?
    resp = continuar()
    if resp == 'N':
        break
    else:
        print("-"*30)
# printando dados na tela
print("-=" * 20)
for i, e in enumerate(pessoas):
    print(f'{i:<3}', e)
print('<<<<< Fim do Programa >>>>')
