from utils import salvar_estoque, carregar_estoque


while True:
    estoque = carregar_estoque('estoque.json')
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
        salvar_estoque(estoque, 'estoque.json')
    elif escolha == '2':   
        from principal import atualizar_quantidade
        atualizar_quantidade(estoque)
        print("Quantidade atualizada com sucesso!")
        salvar_estoque(estoque, 'estoque.json')
    elif escolha == '3':
        from principal import remover_produto
        remover_produto(estoque)
        print("Produto removido com sucesso!")
        salvar_estoque(estoque, 'estoque.json')
    elif escolha == '4':
        from principal import verificar_quantidade
        verificar_quantidade(estoque)
        estoque = carregar_estoque('estoque.json')
    elif escolha == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção invalida. Tente novamente.")
        continue