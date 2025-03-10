print(f'{" Desafio 95 ":-^40}')
time = []
jogador = dict()
gols = list()
resp = 's'
while True:
    tot = 0
    print('-=' * 20)
    print(f'{"CADASTRE O JOGADDOR":^40}')
    jogador['nome'] = str(input('Nome: ').strip().capitalize())
    partidas = int(input('Quantas partidas ele jogou ? '))
    for p in range(0, partidas):
        gols.append(int(input(f'fez quantos gols na partida {p}? ')))
        tot += gols[p]
    jogador['gols'] = gols[:]
    jogador['total'] = tot
    gols.clear()
    time.append(jogador.copy())
    resp = str(input('Quer continuar ? [S/N] ').strip().upper())
    if resp == 'N':
        break
print('--' * 20)
print(f'{"Nº":<10}{"NOME"} {"TOTAL DE GOLS":>20}')
print('-' * 30)
for n, j in enumerate(time):
    print(f'{n:.<10}{j["nome"]:.<15} {j["total"]}')
