lista_compra = []

while True:
    print("===== Menu Princopal =====")
    print("1-Adicionar lista: ")
    print("2-Listar todos os produtos: ")
    print("3-Remover um item pelo indice: ")
    print("4-Sair: ")

    opcao=int(input("Escolha uma opção numérica do menu: "))

    if opcao <1 or opcao >4:
        print("Opção inválida, tente novamente ...")

    elif opcao == 1:
        item_adicionado = input("Escreva o que deseja adicionar a lista de compra: ").lower().strip()
        lista_compra.append(item_adicionado)
        print(f"Item {item_adicionado} foi adicionado com sucesso ...")

    elif opcao == 2:
        if not lista_compra:
            print("A lista de compras esta vazia ...")
        else:
            print("Lista de compras: ")
            for indice , item_adicionado in enumerate(lista_compra):
                print(f"{indice } - {item_adicionado}")
    
    elif opcao == 3: 
        if not lista_compra:
            print("Não há  itens ara ser removido...")
        else:
            remover_item = int(input("digite o número do indice do produto que deseja remover: "))
            lista_compra.pop(remover_item)
            print(f"Item {remover_item} removido com sucesso ...")
    
    elif opcao == 4:
        print("Saindo do sistema ...")
        exit()

    else:
        print("Ops... Ocorreu algum erro no sistema... tente novamente...")
