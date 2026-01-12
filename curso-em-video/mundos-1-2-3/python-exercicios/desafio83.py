print(f'{" Desafio 83 ":=^40}')
ex = input('Digite uma expressão matematica (com parenteses): ')
ex.split()
val = 0
for c in range(0, len(ex)):
    if '(' in ex[c]:
        val += 1
    elif ')' in ex[c]:
        val -= 1
if val == 0:
    print(f'A expressão {ex} é valida !')
else:
    print(f'A expressão {ex} é invalida !')
