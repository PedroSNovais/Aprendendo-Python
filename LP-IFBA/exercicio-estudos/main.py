"""
Sistema de gerenciador de tarefas simples (Sem POO).
Permite ao usuário adicionar, visualizar, editar e excluir tarefas.

Modulo principal do programa.
"""
from utils import receber_inteiro_valido
from arquivo import carregar_tarefas
from funcoes import criar_tarefa
from interface import exibir_menu, listar_tarefas

def executar_sistema():
    """
    Função principal do programa.
    Controla o fluxo do sistema de gerenciador de tarefas.
    """    

    while True:
            lista_tarefas = carregar_tarefas()
            
            exibir_menu()
            opcao = receber_inteiro_valido("Selecione uma opção (0-5): ", maximo=5, minimo=0)

            if opcao == 1:
                print("Opção 1 selecionada")
                criar_tarefa(lista_tarefas)
            elif opcao == 2:
                print("Opção 2 selecionada")
                listar_tarefas(lista_tarefas)
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