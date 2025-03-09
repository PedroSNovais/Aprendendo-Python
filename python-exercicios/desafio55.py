print(f'{"Desafio 55":=^30}')
maiorpeso = 0
menorpeso = 0
for pess in range(1, 6):
    peso = float(input(f'Digite o peso da {pess}ª pessoa:'))
    if pess == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if maiorpeso < peso:
            maiorpeso = peso
        if menorpeso > peso:
            menorpeso = peso
print(f'O maior peso é {maiorpeso}Kg')
print(f'O menor peso é {menorpeso}Kg')
