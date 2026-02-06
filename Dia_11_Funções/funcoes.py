cadastro_principal = []

def menu_principal():
    while True:
        print("--- MENU PRINCIPAL ---")
        print("1 - Cadastro de notas")
        print("2 - Calcular média")
        print("3 - Exibir resultado final")
        print("4 - Sair")
        opcao = input("Escolha a opção numérica: ")
        if opcao <1 or opcao>4:
            print("Opção inválida tente novamente...")
        elif opcao == "1":
            cadastro_Notas()
        elif opcao == "2":
            media = calcular_media()
            print(f"A média das notas é {media:.2f}")
        elif opcao == "3":
            resultado_aprovacao()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

def cadastro_Notas():
    nota = float(input("Digite a nota do aluno: "))
    cadastro_principal.append(nota)

def calcular_media():
    if len(cadastro_principal) == 0:
        print("Nenhuma nota cadastrada.")
        return 0
    media = sum(cadastro_principal) / len(cadastro_principal)
    return media

def resultado_aprovacao():
    media = calcular_media()
    if media >= 7:
        print("Parabéns, você passou de ano!!!")
    else:
        print("Que pena, tente novamente...")


    
    
 
