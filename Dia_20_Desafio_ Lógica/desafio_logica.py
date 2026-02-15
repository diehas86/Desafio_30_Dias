
cadastro_geral = []


##################################################################################
def menu_principal():
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuárioscadastrados")
    print("3 - Buscar um usuário pelo nome")      
    print("4 - Atualizar dados de um usuário")
    print("5 - Remover um usuário")
    print("6 - Encerrar o sistema")
   
    opcao = input("Escolha uma opção numérica do menu: ").strip()

    if not opcao:
        print("Ops acho que você esqueceu de digitar a opção numérica (1,2,3,4,5,6). ")
        return False
  
    if not opcao.isdigit():
        print("Apenas numeros sérão aceitos (1,2,3,4,5,6)...")
        return False
  
    opcao = int(opcao)
  
    if opcao < 1 or opcao >6:
        print("Só serão aceitos numeros entre 1,2,3,4,5,6 ")
        return False
  
    return opcao
#####################################################################################
            

def novo_nome():
    while True:
        nome = input("Digite o nome do novo cadastro: ").strip()
        
        if not nome:
            print("É preciso escrever um nome...")
            continue
    
        if not nome.replace(" ","").isalpha():
            print("Apenas nomes sem números serão aceitos...")    
            continue
    
        if not " " in nome:
            print("Por favor coloque o nome completo...")
            continue   
    
        else:
            print(f"Nome {nome} registrado com sucesso...")
    
        return nome
     
#####################################################################################

def nova_idade():
    while True:
        idade= input("Por favor digite sua idade: ").strip()
    
        if not idade:
            print("Ops acho que vc não escreveu sua idade, tente novamente... ")
            continue
    
        if not idade.isdigit():
            print("A idade precisa ser escrita apenas em números...")
            continue
    
        idade=int(idade)
    
        if idade <18 or idade> 130:
            print("Apenas maiores de idade e idade válidas seerão aceitas...")
            continue
    
        else:
            print(f"A idade {idade} foi cadastrada om sucesso...")
        return idade

#####################################################################################


def novo_email():
    while True:
        email = input("Digite o email para cadastro: ").strip()
        
        if not email:
            print("É necessário escrever um email...")
            continue
        if "@"not in email or "." not in email:
            print("O email precisa ter arroba (@) e ponto (.) ...")
            continue
        
        else:
            print(f"email {email} cadastrado com sucesso...")    
        
        return email

#####################################################################################


def lista_usuários():
    if not cadastro_geral:
        print("A lista de usuários está vazia...")
        return
   
    for usuario in cadastro_geral:
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"Email: {usuario['email']}") 
        print("-" * 30)
    return 

#####################################################################################


def buscar_nome(cadastro_geral):
    if not cadastro_geral:
        print("A lista de usuários está vazia...")
        return None
    
    busca_nome=input("Digite o nome a ser buscado: ").lower().strip()
    
    for usuario in cadastro_geral:
        if usuario["nome"].lower() == busca_nome:
            print("Usuário encontrado.")
            print(f"Nome :{usuario['nome']}")
            print(f"Idade :{usuario['idade']}")
            print(f"Email :{usuario['email']}")
            return usuario
    print("Usuário não encontrado...")
    return None

#####################################################################################


def atualizar_usuario():
    usuario = buscar_nome(cadastro_geral)

    if usuario is None:
        return

    nome = novo_nome()
    if not nome:
        return

    idade = nova_idade()
    if not idade:
        return

    email = novo_email()
    if not email:
        return

    usuario["nome"] = nome
    usuario["idade"] = idade
    usuario["email"] = email

    print("Usuário atualizado com sucesso.")




#####################################################################################


def remover_usuario():
    usuario = buscar_nome(cadastro_geral)
    if  usuario is None:
        return
    cadastro_geral.remove(usuario)
    print(f"Usuario {usuario['nome']} removido da lista com sucesso...")


#####################################################################################

while True:
    opcao=menu_principal()
    
    if opcao is False:
        continue

    if opcao == 1:
        nome = novo_nome()
        if not nome:
            continue

        idade = nova_idade()
        if not idade:
            continue

        email = novo_email()
        if not email:
            continue

        novo_cadastro = {
            "nome": nome,
            "idade": idade,
            "email": email
        }

        cadastro_geral.append(novo_cadastro)

    
    elif opcao == 2:
        opcao = lista_usuários()

    
    elif opcao == 3:
        opcao = buscar_nome(cadastro_geral)

    
    elif opcao == 4:
        opcao = atualizar_usuario()

    
    elif opcao == 5:
        opcao = remover_usuario()
    
    elif opcao == 6:
        print("Saindo do sistema ...")
        break


