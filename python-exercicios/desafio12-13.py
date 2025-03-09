# 12  de 5% de desconto num produto
print('{:=^30}'.format('Desafio 12'))
v = float(input('Qual o valor do produto que vc quer aplicar o desconto ?'))
pc = float(input('qual o valor do desconto que vc quer apliar ? ( em %)'))
d = v*pc/100
print(f'Com a aplicação do desconto de {pc}% o produto passa a custar {v-d:.2f}')

# 13 faça um prograga que da 15% de aumento pra um funcionario
print('{:=^30}'.format('Desafio 13'))
sal = float(input('Qual o salario do funcionario ?'))
pc = float(input('Qual o aumento do funcionario ? (em %)'))
au = sal*pc/100
print(f'O salario do funcionario que recebia {sal:.2f} com o aumento receberá {sal+au:.2f}')
