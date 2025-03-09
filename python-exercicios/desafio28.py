from random import randint
print(f'{"Desafio 28":=^50}')
print(f'\033[35m{"JOGO DE ADIVINHAÇÃO":*^50}\033[m !')
num = randint(0, 5)
print(f'O computador gerou um numero entre 0 e 5')
p = int(input('De um palpite de qual foi o numero gerado:'))
if p == num:
    print(f'Parabens! O número gerado foi realmente {num}.')
else:
    print(f'Você errou! O número gerado foi {num}! ')
print(f'{"Fim de Jogo":=^30}')
