print(f'{"Desafio 56":=^30}')
media = 0
velho = 0
femininomv = 0
for analise in range(1, 5):
    print(f'--- {analise}ª PESSOA ---')
    nome = str(input(f'NOME: ')).strip().upper()
    idade = int(input(f'IDADE: '))
    sexo = str(input(f'SEXO [M/F]: ')).strip().upper()
    media = media + idade
    if sexo == 'M' and idade > velho:
        velho = idade
        nvelho = nome
    if sexo == 'F' and idade > 20:
        femininomv += 1
print(f'A media das idades é {media/4:.1f} anos.')
print(f'O nome do Homem mais velho é {nvelho} com {velho} anos.')
print(f'São {femininomv} mulheres menores de 20 anos.')
