# desafio 36 "aprovando emprestimo"
print(f'\033[1;30m{"Desafio 36":=^30}\033[m')
vcasa = float(input('Quantos R$ custa a casa que você pretende comprar ? '))
salario = float(input('Qual o valor do seu salario (R$)? '))
tempo = int(input('quantos anos de financiamento ?'))
tempo = tempo * 12
parcela = vcasa // tempo
maximo = (salario * 30) / 100
if parcela > maximo:
    print(f'\033[4;31;40m Financiamento Negado!!!\033[m'
          f'\nVocê não conseguiria pagar esse financiamento com o salario atual!')
else:
    print(f'\033[4;32;40m O Seu Financiamento foi aprovado \033[m\n '
          f'O valor da parcela é {parcela:.2f}R$ e você pagará em {tempo} meses')
