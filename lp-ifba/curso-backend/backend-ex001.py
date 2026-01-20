class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.velocidade = 0
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
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


v1 = Veiculo("fiat", "fusca", 1994)
v1.acelerar()
v1.frear()
v1.exibir_dados()
