cadastro = {}

while True:
    print("===== Menu =====")
    print("1-Cadastro de usuário")
    print("2-Acessar usuário")
    print("3-Mostrar todos os cadastros")
    print("4-Sair")
    
    
    try:
        entrada = input("Digite a opção numérica do menu: ")
        if not entrada.strip():
            print("Você não digitou nada, Digite as opções numéricas (1,2,3)")
            continue
        opcao = int(entrada)
    except:
        print("Digite apenas as  opções numéricas do menu(1,2,3)")
        continue
    
    
    if opcao == 1:
        nome = input("Digite o nome para cadastro: ").strip()
        idade = int(input("Digite a idade para cadastro: ")) 
        cadastro [nome] = idade
        print (f"O nome {nome} e a idade {idade} foram cadastradas com sucesso ...")

    
    elif opcao == 2:
        if not cadastro:
            print("Nenhum usuário cadastrado")  
        else:
            busca_nome = input("Digite o nome a ser procurado: ").strip()
            idade = cadastro.get (busca_nome)
            print(f"{busca_nome} tem {idade} anos ...")
    
    
    elif opcao == 3:
        if not cadastro:
            print("Nenhum nome cadastrado...")
        else:
            for nome, idade in cadastro.items():
                print(f"Nome:{nome} idade: {idade}")
    

    elif opcao == 4:
        print("Saindo do programa ...")
        break


    else:
        print("Algo deu errado, pode ser um erro no código se isso voltar a acontecer revisite o codigo fonte")


    

