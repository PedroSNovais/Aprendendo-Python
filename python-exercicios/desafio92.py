from datetime import date
print(f'{" Desafio 92 ":-^40}')
pessoa = dict()
pessoa['Nome'] = str(input('Nome: ').strip().capitalize())
nascimento = int(input('Ano de Nascimento:'))
pessoa['idade'] = date.today().year - nascimento
pessoa['clt'] = int(input('Nº carteira de trabalho: ( 0 = não possui )'))
if pessoa['clt'] != 0:
    pessoa['contratação'] = int(input('Qual o ano de contratação ? '))
    pessoa['salário'] = float(input('Qual o Salário ? '))
    tempo = date.today().year - pessoa['contratação']
    pessoa['aposentadoria'] = (35 - tempo) + pessoa['idade']
print('-=' * 30)
for k, v in pessoa.items():
    print(f' - {k} tem valor {v}')
