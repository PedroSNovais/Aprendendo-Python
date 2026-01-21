from ex001.classeex001 import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)