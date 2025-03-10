def titulo(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))


print(f'{" Desafio 97 ":-^40}')
for c in range(0, 3):
    m = str(input('Digite a mensagem 1: '))
    titulo(m)
