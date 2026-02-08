lista_tarefas = []

def menu():
    print("=== Menu Principal ===")
    print("1-Adicionar tarefas: ")
    print("2-Listar tarefas: ")
    print("3-Encerrar programa: ")
    
    


def adicionar_tarefa():
    adicionar = input("Descreva a tarefa realizada: ").strip()
    if not adicionar:
        print("A lista descrita não pode estar vazia, esse erro pode acontecer se você apertar o ENTER sem escrever nada...")
    else:
        lista_tarefas.append(adicionar)
        print(f"A tarefa {adicionar} foi adicionada com sucesso") 
    

def listar_tarefas():
    if not lista_tarefas:
        print("A lista de tarefas está vazia...")
    else:
        for indice, tarefa in enumerate(lista_tarefas, start=1):
            print (f"{indice}. {tarefa}")
    


while True:
    menu()
    try:
        opcao = int(input("Digite o número referente a escolha do menu: "))
    except ValueError:
        print("Digite apenas números validos ...")
        continue
    
       
    if opcao == 1:
        adicionar_tarefa()
            
    
    elif opcao == 2:
        listar_tarefas()

    
    
    elif opcao == 3:
        print("Saindo do programa ...")
        break
    
    
    else:
        print("Opção inválida. Se o erro persistir, verifique o código.")

            