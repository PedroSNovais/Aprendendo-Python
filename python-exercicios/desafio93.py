print(f'{" Desafio 93 ":-^40}')
jogador = dict()
gols = []
total = 0
jogador['nome'] = str(input('Qual o nome do jogador ? ').strip().capitalize())
jogos = int(input('Quantas partidas ele jogou ? '))
jogador['gols'] = gols
print('--' * 20)
for j in range(0, jogos):
    gols.append(int(input(f'Quantos gols ele fez na partida {j} ? ')))
    total += gols[j]
jogador['total'] = total
print('-=' * 30)
print((jogador.items()))
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
for j in range(0, jogos):
    print(f'    => Na partida {j}, fez {gols[j]} gols.')
print(f'Foi um total de {total} gols')