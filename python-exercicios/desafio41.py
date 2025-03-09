from datetime import date
print(f'{"Desafio 41":=^30}')
nasc = int(input('Digite o ano de nascimento do atleta: '))
hoje = date.today().year
idade = hoje - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print(f'O atleta que tem {idade} anos é da classe \033[36mMIRIM\033[m')
elif  9 < idade <= 14:
    print(f'O atleta de {idade} anos é da classe \033[36mINFANTIL\033[m')
elif 14 < idade <= 19:
    print('Pertence a classe \033[35mJUNIOR\033[m')
elif 19 < idade <= 25:
    print('Pertence a classe \033[33mSÊNHOR\033[m ')
elif 25 < idade <= 100:
    print(f'Pertence a classe \033[31mMASTER\033[m')
else:
    print(f'Você não pode competir!')
