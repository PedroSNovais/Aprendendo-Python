''' 
Produzi os arquivos com esse nome a partir do estudo do material do Curso: desenvolvimento back end com python do 
projeto: Capacitação 4 - Conecta e Capacita 
Bolsa Futuro Digital - IFBA PS
Instrutora: Ana Cristina O Linhares
 '''

# Criando a classe 
class Pessoa:
   
    peso = 0
    altura = 0.0

    def __init__(self, nome, idade):
        self.nome = nome.upper()
        self.idade = idade

    def apresentar(self):
        print(f'O nome da pessoa é {self.nome} e ela tem {self.idade} anos de idade')
   
    def aniversario(self):
        self.idade += 1
        print(f'{self.nome} agora tem {self.idade} anos')

    def calcular_IMC(self):
        print(f"{self.nome} tem o IMC de: {self.peso / (self.altura ** 2)}")
    
    def alterar_peso(self, novo_peso):
        self.peso = novo_peso

    def alterar_altura(self, nova_altura):
        self.altura = nova_altura
    
    def verificar_maioridade(self,):
        if self.idade >= 18:
            print(f"{self.nome} é maior de idade !!")
        else:
            print(f"{self.nome} NÃO é maior de idade !!")
        
    def comparar_idades(self, outra_Pessoa): #  " outra_Pessoa " deve ser outro objeto da mesma classe
        
        if self.idade == outra_Pessoa.idade:
            print(f"{self.nome} e {outra_Pessoa.nome} tem a mesma idade !!")
        elif self.idade > outra_Pessoa.idade:
            print(f"{self.nome} é mais velho(a) que {outra_Pessoa.nome}")
        else:
            print(f"{outra_Pessoa.nome} é mais velho(a) que {self.nome}")

# Instanciando a Classe

p1 = Pessoa("maria", 5)
p1.apresentar()
p1.verificar_maioridade()

print("------------------")

p2 = Pessoa("Paulo", 30)
p2.alterar_altura(1.80)
p2.alterar_peso(100)
p2.apresentar()

print("_________________________")

p1.comparar_idades(p2)

