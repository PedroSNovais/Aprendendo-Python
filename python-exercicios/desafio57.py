print(f'{"Desafio 57":=^30}')
nome = str(input('Qual o nome da pessoa:'))
sexo = ''
while sexo not in ['M', 'F']:
    sexo = str(input('Qual o sexo da pessoa ? [M/F] ')).strip().upper()
    if sexo not in ['M', 'F', 'MASCULINO', 'FEMININO']:
        print('Não existe essa opção. TENTE NOVAMENTE!')
print(f'{nome} é do sexo {sexo}')
