lista_compras = []
while True:
    print("\n--- Menu Lista de Compras ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item a adicionar: ")
        lista_compras.append(item)
        print(f"'{item}' adicionado à lista.")
    elif opcao == "2":
        item = input("Digite o item a remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' removido da lista.")
        else:
            print(f"'{item}' não encontrado na lista.")
    elif opcao == "3":
        if lista_compras:
            print("\n--- Sua Lista de Compras ---")
            for i, item in enumerate(lista_compras):
                print(f"{i + 1}. {item}")
        else:
            print("Sua lista de compras está vazia.")
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
