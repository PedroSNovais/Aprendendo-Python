print('{:=^30}'. format('Desafio 15'))
c = float(input('Digite uma temperatura em ºC:'))
f = ((9 * c) / 5)+32
print(f'{c}ºC são {f}ºF !')

print('{:=^30}'.format('Desafio 16'))
dias = int(input('Por quantos dias o carro foi alugado ?'))
km = float(input('Quantos kilometros o carro percorreu ?'))
vd = dias*60
vkm = km*0.15
print(f'você tem que pagar {vd+vkm:.2f}R$ por utilizar esse carro ! ')
