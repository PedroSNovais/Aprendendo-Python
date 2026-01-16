class Animal: # Criando a classe 

    def __init__(self, nome, especie, idade, peso): #Criando o magic metod (Construtor)
    # atributos obrigatorios na criação
        self.nome = nome.upper()    
        self.especie = especie.upper()
        self.idade = idade
        self.__peso = peso
    
    def get_peso(self):
        return self.__peso
    
    def set_peso(self, novo_peso):
        if novo_peso <= 0:
            print(f"impossivel atribuir peso negativo ao {self.nome}")
        else:
            self.__peso = novo_peso

    def alimentar(self, quantidade):
        self.set_peso(self.get_peso() + (quantidade * 0.2))
        print(f"O {self.nome} foi alimentado")
    
    def emitir_som(self,):
        print(f"{self.nome} está emitindo som...")
    
    def envelhecer(self):
        self.idade += 1

    def apresentar(self):
        print(f"""
            NOME: {self.nome}
            ESPÉCIE: {self.especie}
            IDADE: {self.idade}
            PESO: {self.get_peso()}
        ___________________________
                """)
        



# Criando subclasse cachorro
class Cachorro(Animal):
    # adicionando coisas ao método construtor
    def __init__(self, nome, especie, idade, peso):
        super().__init__(nome, especie, idade, peso)
        self.especie = "Cachorro"

    # sobreescrevendo um metodo da classe mãe
    def emitir_som(self):
        print(f'O Cachorro {self.nome} diz: AU AU !!')





# Criando classe filha Gato
class Gato(Animal):
    # Adicionando coisas a um método ja existente na classe mãe
    def __init__(self, nome, especie, idade, peso):
        super().__init__(nome, especie, idade, peso)
        self.especie = "Gato"

    # Sobreescreve um método da clase mãe para funcionar completamente diferente
    def emitir_som(self):
        print(f'O gatinho {self.nome} diz: MIAU MIAU !! ')


# instanciando
animal1 = Gato("chico", "gato", 1, 8)
animal2 = Animal("badaró", "sapo", 2, 0.2)
animal3 = Animal("dolle", "capivara", 5, 10.2)
animal4 = Cachorro("ZEZE", "Cachorro", 1, 6.2)
animal5 = Gato("Tom", 'gato', 6, 2.5)

#executando métodos

animal1.apresentar()
animal2.apresentar()
animal3.apresentar()
animal4.apresentar()
animal5.apresentar()

animal1.emitir_som()
animal3.emitir_som()
animal4.emitir_som()

animal2.alimentar((-30))

