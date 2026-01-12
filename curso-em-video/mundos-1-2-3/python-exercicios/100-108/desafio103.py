from teste import titulo


def ficha(nome='<desconhecido>', gols='0'):
    print(f'O jogador {nome} fez {gols} gols !')


titulo(' Desafio 103')
n = str(input('Nome: ').strip().capitalize())
g = str(input('Quantos gols o jogador fez ? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
