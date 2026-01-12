print(f'{"Desafio 33":=^30}')
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite o ultimo numero:'))
# testando o menor
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
# testando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
