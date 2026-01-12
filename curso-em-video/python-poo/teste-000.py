class vendedor():
    
    def __init__(self, nome: str ) -> None:
        self.nome = nome
        self.valor_vendas = 0

    def vendeu(self, valor: float) -> None:
        self.valor_vendas = valor
        print(self.nome, f"vendeu R${self.valor_vendas:.2f}")

pedro = vendedor("Pedro")
pedro.vendeu(0)