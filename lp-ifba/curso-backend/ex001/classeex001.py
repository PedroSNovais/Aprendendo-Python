# criando a class
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__velocidade = 0
        self.__marca = marca
        self.__modelo = modelo
        self.ano = ano

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
        if nova_velocidade >= 0 and nova_velocidade <= 200:
            self.__velocidade = nova_velocidade
        else: 
            print("Não é possivel atribuir esse valor para velocidade !!")
    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, novo_ano):
        if novo_ano >= 1900:
            self.__ano = novo_ano
        else:
            print("não é possivel cadastrar um carro com esse ano de fab")
            self.ano = 1900

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
            Velocidade Atual: {self.velocidade}Km/h""") 
    def parar(self):
        self.velocidade = 0

    def tempo_uso(self):
        from datetime import date
        ano_atual = date.today().year
        print(f"Esse veiculo tem {ano_atual - self.ano} anos de uso")

    def falar(self):
        print("vrum, vrum !!")   
            

