"""
Sistema de gerenciador de tarefas simples (Sem POO).
Permite ao usuário adicionar, visualizar, editar e excluir tarefas.

Modulo principal do programa.
"""
from utils import (receber_inteiro_valido, exibir_menu)
from arquivo import salvar_tarefas, carregar_tarefas

def executar_sistema():
    """
    Função principal do programa.
    Controla o fluxo do sistema de gerenciador de tarefas.
    """    
    tareras = carregar_tarefas()
    
    while True:
            exibir_menu()
            opcao = receber_inteiro_valido("Selecione uma opção (0-5): ", maximo=5, minimo=0)

            if opcao == 1:
                print("Opção 1 selecionada")
                # Adicione aqui o código para a opção 1
            elif opcao == 2:
                print("Opção 2 selecionada")
                # Adicione aqui o código para a opção 2
            elif opcao == 3:
                print("Opcão 3 selecionada")
                # Adicione aqui o código para a opção 3
            elif opcao == 4:
                print("Opção 4 selecionada ")
                # Adicione aqui o código para a opção 4
            elif opcao == 5:
                 print("Opção 5 selecionada ")
                # Adicione aqui o código para a opção 5
            elif opcao == 0:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar_sistema()