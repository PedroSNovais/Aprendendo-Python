from de112.uteiscev import moeda
from de112.uteiscev import dado
p = dado.leiadinheiro('Digite um valor: R$')
print(p)
moeda.resumo(p, 80, 25)
