from uteis115 import *
print(f'{" Desafio 115 ":*^40}')
pessoas = list()
while True:
    p = dados()
    resp = continuar()
    if len(p['snome']) == 0:
        pessoas.append(f'{p["nome"][0]:<10} {p["idade"]} anos')
    else:
        pessoas.append(f'{p["nome"][0]} {p["snome"][p["lsn"]]} {p["idade"]:>10} anos')
    if resp == 'N':
        break
    else:
        print("-"*30)
print("-=" * 20)
for i, e in enumerate(pessoas):
    print(f'{i:<3}', e)
print('<<<<< Fim do Programa >>>>')