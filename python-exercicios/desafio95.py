print(f'{" Desafio 95 ":-^40}')
time = []
jogador = dict()
gols = list()
while True:
    resp = 'a'
    tot = 0
    print('-=' * 20)
    print(f'{"CADASTRE O JOGADDOR":^40}')
    jogador['nome'] = str(input('Nome: ').strip().capitalize())
    partidas = int(input('Quantas partidas ele jogou ? '))
    jogador['partidas'] = partidas
    for p in range(0, partidas):
        gols.append(int(input(f'fez quantos gols na partida {p}? ')))
        tot += gols[p]
    jogador['gols'] = gols[:]
    jogador['total'] = tot
    gols.clear()
    time.append(jogador.copy())
    while resp not in 'sSnN':
        resp = str(input('Quer continuar ? [S/N] ').strip().upper())
    if resp == 'N':
        break
print('--' * 20)
print(f'{"codº":<10}{"NOME"} {"TOTAL DE GOLS":>20}')
print('-' * 30)
for n, j in enumerate(time):
    print(f'{n:.<10}{j["nome"]:.<15} {j["total"]}')
print('-=' * 30)
while True:
    n = (int(input('Digite o codº do jogador para ver seu desempenho: ( 999 = parar ) ')))
    if n == 999:
        break
    elif n >= len(time):
        print(f'O jogador com o codº {n} não foi cadastrado... ')
    else:
        print("--" * 30)
        print(f'LEVANTAMENTO DO JOGADOR {time[n]["nome"]}...')
        print(f'O jogador "{time[n]["nome"]}" jogou {time[n]["partidas"]} partidas.')
        for p in range(0, time[n]['partidas']):
            print(f' => Na partida {p}, fez {time[n]["gols"][p]} gols')
        print(f'No total foram {time[n]["total"]} gols')
    print("--" * 30)
print(f'<<< FIM DO PROGRAMA >>>')
