def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno de {comp}x{larg}m é {a}m !')


print(f'{" Desafio 96 ":-^40}')
print(f'{"Medidor de Área":^40}\n', '-' * 40)
la = float(input('Largura: (m) '))
c = float(input('comprimento: (m) '))
area(la, c)
