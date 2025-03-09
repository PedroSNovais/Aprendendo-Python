frase = str(input('Digite uma frase:')).strip()
frase = frase.lower()
print(f'A letra "A" aparece {frase.count("a")} vezes')
print(f'A letra "A" apareceu primeiro na posição {frase.find("a")+1}')
print(f'A ultima letra "A" apareceu na posição {frase.rfind("a")+1}')

# desafio 27
print('{:=^30}'.format('Desafio 27'))
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer!!')
print(f'Seu primeiro nome é "{n[0]}"')
print(f'Seu ultimo nome é "{n[len(n)-1]}"')
