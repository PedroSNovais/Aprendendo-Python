from datetime import date
print(f'{"Desafio 54":=^30}')
atual = date.today().year
maioridade = 0
menoridade = 0
for c in range(1, 8):
    ano = int(input(f'digite o ano de nascimento da {c}ª pessoa:'))
    if atual - ano >= 21:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print(f'{maioridade} pessoas dessa lista são maiores de 21 anos!')
print(f'{menoridade} pessaoas dessa lista são menores de 21 anos!')
