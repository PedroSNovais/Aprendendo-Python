estoque = {}

while True:
    print("\nMenu de Opções:")
    print("1. Adicionar Produto")
    print("2. Atualizar Quantidade")
    print("3. Remover Produto")
    print("4. Verificar Quantidade")
    print("5. Sair")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '1':
        from principal import adicionar_produto
        adicionar_produto(estoque)
        print("Produto adicionado com sucesso!")
        print(estoque)

    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção invalida. Tente novamente.")
        continue