from classeex001 import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.__portas = portas
        self.__capacidade_carga = capacidade_carga
    
    def falar(self):
        print("Vruuuuumm!")

# adicionando funcionalidades a um método já existente
    def exibir_dados(self):
        super().exibir_dados()
        print(f"""
            Portas: {self.__portas}
            Capacidade de carga: {self.__capacidade_carga}""")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, portas, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.__portas = portas
        self.__capacidade_carga = capacidade_carga

    def falar(self):
        print("Brrrumm!")

        # adicionando funcionalidades a um método já existente
    def exibir_dados(self):
        super().exibir_dados()
        print(f"""
            Portas: {self.__portas}
            Capacidade de carga: {self.__capacidade_carga}""")

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, portas, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.__portas = portas
        self.__capacidade_carga = capacidade_carga
    
    def falar(self):
        print("Honkk!")

    # adicionando funcionalidades a um método já existente
    def exibir_dados(self):
        super().exibir_dados()
        print(f"""
            Portas: {self.__portas}
            Capacidade de carga: {self.__capacidade_carga}""")