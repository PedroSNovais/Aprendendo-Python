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
        if self.__peso <= 0:
            print("impossivel atribuir peso negativo")
        else:
            self.__peso = novo_peso

    def emitir_som(self,):
        print(f"{self.nome} está emitindo som...")
    
    def envelhecer(self):
        self.idade += 1

    def apresentar(self):
        print(f"""
            NOME: {self.nome}
            ESPÉCIE: {self.especie}
            IDADE: {self.idade}
        ___________________________
                """)
        

# instanciando
animal1 = Animal("chico", "gato", 1)
animal2 = Animal("badaró", "sapo", 2 )
animal3 = Animal("dolle", "capivara", 5)

#executando métodos
animal1.emitir_som()
animal3.emitir_som()
animal1.apresentar()
animal2.apresentar()
animal3.apresentar()
