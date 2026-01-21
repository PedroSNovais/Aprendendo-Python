from classeex001 import Veiculo
from subclasses import Carro, Moto, Caminhao
# instanciando objeto da classe mãe
v1 = Veiculo("fiat", "fusca", 1800)
v1.acelerar()
v1.acelerar()
v1.frear()
v1.exibir_dados()
print("-----------------------------------")

lista_veiculos = [Carro("Fiat", "Uno", 1000, 2, 'media'), Caminhao("Mercedes", "Bens", 2020, 2, "alta"),Carro("Jeep", "Renegad", 2024, 4, 'media'), Moto("Honda", "Bros", 2025, 0, "baixa")]

for veiculo in lista_veiculos:
    veiculo.exibir_dados()
    print("-----------------------------------")