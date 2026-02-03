lista_compras = []

while True:
    print("=====Menu principal=====")
    print('1-'"Adicionar itens na lista: ")
    print('2-'"Remover itens: ")
    print('3-'"Verificar se um item está na lista: ")
    print('4-'"Mostrar todos os itens da lista: ")
    print('5-'"sair")
    escolha= int(input("Escolha o numero correspondente: "))

    if  escolha == 1:
        adicionar_item= input("Escreva o item a ser adicionado na lista: ") 
        lista_compras.append (adicionar_item)
        print("Item adicionado com sucesso...")

    elif escolha == 2:
        remover_item = input("Escreva o item que deseja remover da lista: ")
        lista_compras.remove(remover_item)
        print(f"O item {remover_item} foi removido com sucesso ...")

    elif escolha == 3:
        verificar_item = input("Escreva o item para ser verificado: ")
        if  verificar_item in lista_compras:
            print("Produto cadastrado na lista de compras...")
        else:
            print("Produto não cadastrado na lista de compras...")
 
    elif escolha == 4:
        for lista_completa in lista_compras:
            print (f"{lista_completa}")

    elif escolha == 5:
        print("Saindo do programa ...")
        break
    else:
        print("Ops...Erro no programa...")

