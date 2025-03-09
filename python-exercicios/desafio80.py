print(f'{" Desafio 80 ":=^40}')
num = []
for cont in range(0, 5):
    n = (int(input('Digite um numero: ')))
    if cont == 0 or n >= num[-1]:
        num.append(n)
        print('Adicionado ao fim da lista...')
    elif n <= num[0]:
        num.insert(0, n)
        print('Adicionaddo na posição 0 da lista...')
    else:
        c = 0
        while c < cont:
            if n < num[c]:
                num.insert(c, n)
                print(f'Adiocionado na posição {c} da lista...')
                break
            c = c + 1
print('-='*30)
print('Os valores digitados em oordem foram', num)
