print(f'{"Desafio 31":=^30}')
dist = int(input('Digite a distancia da sua viagem em km:'))
if dist < 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print(f'O valor da passagem para essa distancia é {valor:.2f} R$.')
