lista_tarefas = []

while True:
    print("\n===== Menu Principal =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa pelo índice")
    print("4 - Sair")

    opcao = input("Escolha uma opção numérica do menu: ")

    if not opcao.isdigit():
        print("Opção inválida. Digite apenas números.")
        continue

    opcao = int(opcao)

    if opcao < 1 or opcao > 4:
        print("Opção inválida. Escolha entre 1 e 4.")

    elif opcao == 1:
        tarefa = input("Digite a tarefa: ").strip().lower()

        if tarefa == "":
            print("Não é possível adicionar uma tarefa vazia.")
        else:
            lista_tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso.")

    elif opcao == 2:
        if not lista_tarefas:
            print("Lista de tarefas vazia.")
        else:
            print("\nLista de tarefas:")
            for indice, tarefa in enumerate(lista_tarefas):
                print(f"{indice} - {tarefa}")

    elif opcao == 3:
        if not lista_tarefas:
            print("Não há tarefas para remover.")
            continue

        indice = input("Digite o índice da tarefa que deseja remover: ")

        if not indice.isdigit():
            print("Digite um número válido.")
            continue

        indice = int(indice)

        if indice < 0 or indice >= len(lista_tarefas):
            print("Índice inexistente.")
        else:
            removida = lista_tarefas.pop(indice)
            print(f"Tarefa '{removida}' removida com sucesso.")

    elif opcao == 4:
        print("Saindo do programa...")
        break

