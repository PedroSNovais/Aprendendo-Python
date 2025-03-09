nome = str(input('qual o seu nome ?'))
if nome == 'pedro':
    print('que nome bonito !!')
elif nome in 'maria joao jose':
    print('que nome de velho !')
else:
    print(f'que nome normal')
num = int(input('Digite um numero:'))
if num > 10:
    print('seu numero é maior que 10')
    if num < 20:
        print('seu numero esta entre 10 e 20')

