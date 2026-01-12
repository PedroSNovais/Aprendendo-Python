print(f'{"Desafio 34":=^30}')
salario = float(input('Digite o salario de um funcionario:'))
if salario <= 1250.0:
    p = str('15%')
    al = salario + ((salario * 15)//100)
else:
    p = str('10%')
    al = salario + ((salario * 10)//100)
print(f'O salario do funcionario após um aumento de {p} passa a ser {al} R$.')
