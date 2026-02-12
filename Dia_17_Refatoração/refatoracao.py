cadastro = []
def menu_principal():
    print("1 - Cadastrar nome")
    print("2 - Listar nomes")
    print("3 - Sair")
   


def cadastrar_nome():
    if not nome.strip():
        print("o nome não pode ser em branco tente novamente")
    else:
        cadastro.append(nome)
        print(f"{nome} Cadastrado com sucesso")
   


def listar_nomes (lista_completa):
    if not lista_completa:
        print("A lista de nomes está vazia...")
    else:
        for nome in lista_completa:
            print(nome)
          



while True: 
    menu_principal()
    menu= input("Digite a opção numérica do menu: ")
    
    if not menu.isdigit():
        continue
            
    if menu not in ['1','2','3']:
        print("Digite apenas números válidos (1,2,3)")
        continue
    
    menu=int(menu)
    
    if menu == 1:

        nome=input("Digite o nome para cadastro: ")
        cadastrar_nome()

    if menu == 2:
        listar_nomes(cadastro)  
    
        
    elif menu == 3:
        print("Saindo do programa ...")
        break


