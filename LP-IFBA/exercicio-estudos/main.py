"""
Sistema de gerenciador de tarefas simples (Sem POO).
Permite ao usuário adicionar, visualizar, editar e excluir tarefas.

Modulo principal do programa.
"""
from utils import menu

def executar_sistema():
    """
    Função principal do programa.
    Controla o fluxo do sistema de gerenciador de tarefas.
    """    
    
    while True:
            resposta = menu()

            if resposta == 1:
                print("Opção 1 selecionada")
                # Adicione aqui o código para a opção 1
            elif resposta == 2:
                print("Opção 2 selecionada")
                # Adicione aqui o código para a opção 2
            elif resposta == 3:
                print("Opcão 3 selecionada")
                # Adicione aqui o código para a opção 3
            elif resposta == 4:
                print("Opção 4 selecionada ")
                # Adicione aqui o código para a opção 4
            elif resposta == 5:
                 print("Opção 5 selecionada ")
                # Adicione aqui o código para a opção 5
            elif resposta == 0:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()