# desafio 24
print('{:=^30}'.format('Desafio 24'))
nc = str(input('Digite o nome da sua cidade:')).strip()
nc = nc.lower()
nc = nc.split()
s = nc[0]
s.find('santo')
if 'santo' in s:
    print('\033[1;30;42mO nome da sua cidade começa com "santo"!!\033[m')
else:
    print(f'\033[1;30;43mA sua cidade não começa com "santo"!!\033[m')
# Desafio 25
print('{:=^30}'.format('Desafio 25'))
nome = str(input('Digite o seu nome:'))
nome = nome.strip()
nome = nome.lower()
if 'silva' in nome:
    print(f'\033[1;30;42mVocê possui "silva" no seu nome, que legal !!!\033[m')
else:
    print(f'\033[1;30;43mVocê é diferente dos normais !\033[m')