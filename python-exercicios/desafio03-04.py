print('      ============ Desafio 03 ===============               ')

n1 = int(input('digite um número:'))
n2 = int(input('Digite outro numero:'))
s = n1 + n2
print('A soma entre {0} e {1} vale {2} !'.format(n1, n2, s))

print('      ============ Desafio 04 ===============')

a = input('Digite algo:')
print(                                            )
print('A classe do que foi digitado é: ', type(a))
print('O que foi digitado é composto de espaços?', a.isspace())
print('O que foi digitado é numerico ? ', a.isnumeric())
print('O que foi digitado é compósto de letras ? ', a.isalpha())
print('o que foi digitado é alfanumerico ?', a.isalnum())
print('está em MAIÚSCULAS ?', a.isupper())
print('está em minúsculas ?', a.islower())
print('está Capitalizada ?', a.istitle())