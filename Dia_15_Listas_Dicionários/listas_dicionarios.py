lista_pedidos = []

while True:
    print("===== MENU PRINCIPAL =====")
    print("1- Cadastro de novos pedidos:")
    print("2-Lista de pedidos:")
    print("3-Sair")

    try:
        valor_numerico = input("Digite a opção numérica do menu: ")
        if not valor_numerico.strip():
            print("Digite apenas números (1,2,3)")
            continue
        opcao = int(valor_numerico)   

    except ValueError:
        print("Opção inválida, só são permitidos números (1,2,3)")
        continue

    if opcao == 1:
        novo_cliente = input("Escreva o nome do cliente: ")
        if not novo_cliente.strip():
            print("O nome do cliente precisa ser escrito ...")
            continue
        cadastro_cliente = (novo_cliente)



        novo_produtos = input("Escreva o produto adiquirido: ")
        if not novo_produtos.strip():
            print("É necessário cadasrtar o produto adquirido, não pode estar com nome vazio ...")        
            continue
        cadastro_produtos =(novo_produtos)
        
        
     
        total = input("Digite o valor total do pedido: ")
        if not total:
            print("O valor total não pode estar vazio digite um valor válido...")
            continue
    
        try:
            cadastro_valor_total = float (total)
        except ValueError:    
            print("Digite um valor numérico para o total gasto com o pedido...")
            continue

        cadastro_completo = {"cliente":cadastro_cliente,
                             "produto":cadastro_produtos,
                             "valor_total":cadastro_valor_total}
        
        lista_pedidos.append(cadastro_completo)
    
    elif opcao == 2:
        if not lista_pedidos:
            print("A lista de pedidos está vazia ...")
            continue
        for pedido in lista_pedidos:
                               print(f"""Nome do cliente: {pedido['cliente']}
            Nome do produto: {pedido['produto']}
            Valor total: {pedido['valor_total']:.2}""")
    
    elif opcao == 3:
        print("Saindo do programa ...")
        break
              
    
