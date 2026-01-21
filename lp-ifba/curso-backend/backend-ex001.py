# criando a class
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__velocidade = 0
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

# gatters e setters

    # get da marca
    @property 
    def marca(self):
        return self.__marca
     # set da marca
    @marca.setter
    def idade(self, nova_marca):
        self.__marca = nova_marca

    @property # get do modelo
    def modelo(self):
        return self.__modelo
    @modelo.setter # set do modelo
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    @property
    def velocidade(self):
        return self.__velocidade
    @velocidade.setter
    def velocidade(self, nova_velocidade):
        if nova_velocidade >= 0:
            self.__velocidade = nova_velocidade
        else: 
            print("Não é possivel atribuir um valor negativo a essa variavel !!")
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

# métodos normais

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
        else:
            print("O veiculo está parado")

    def exibir_dados(self):
        print(f"""
            Marca: {self.marca}
            Modelo: {self.modelo}
            Ano: {self.ano}
            Velocidade Atual: {self.velocidade}Km/h
                """) 
            
# instanciando objeto
v1 = Veiculo("fiat", "fusca", 1994)
v1.acelerar()
v1.acelerar()
v1.frear()
v1.exibir_dados()
