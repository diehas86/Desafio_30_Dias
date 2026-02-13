chamadas_suporte = []
status_validos = ["aberto", "andamento", "finalizado"]


def cadastro_chamada():
    nome = input("Digite seu nome: ").strip()

    if not nome:
        print("O nome não pode estar vazio.")
        return None

    if not nome.replace(" ", "").isalpha():
        print("O nome deve conter apenas letras.")
        return None

    if " " not in nome:
        print("Digite nome e sobrenome.")
        return None

    print("Nome cadastrado com sucesso.")
    return nome


def descricao_problema():
    descricao = input("Descreva o problema: ").strip()

    if not descricao:
        print("A descrição não pode estar vazia.")
        return None

    print("Descrição cadastrada com sucesso.")
    return descricao


def status_problema():
    status = input("Digite o status (aberto, andamento, finalizado): ").strip().lower()

    if not status:
        print("O status não pode estar vazio.")
        return None

    if status not in status_validos:
        print("Status inválido.")
        return None

    return status


while True:
    print("\n=== MENU DE SUPORTE ===")
    print("1 - Cadastrar nova chamada")
    print("2 - Listar chamadas")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if not opcao.isdigit():
        print("Digite apenas números (1, 2 ou 3).")
        continue

    opcao = int(opcao)

    if opcao == 1:
        nome = None
        while nome is None:
            nome = cadastro_chamada()

        descricao = None
        while descricao is None:
            descricao = descricao_problema()

        status = None
        while status is None:
            status = status_problema()

        chamada = {
            "nome": nome,
            "descricao": descricao,
            "status": status
        }

        chamadas_suporte.append(chamada)
        print("Chamada registrada com sucesso.")

    elif opcao == 2:
        if not chamadas_suporte:
            print("Nenhuma chamada registrada.")
        else:
            for i, chamada in enumerate(chamadas_suporte, 1):
                print(
                    f"{i} - Nome: {chamada['nome']} | "
                    f"Descrição: {chamada['descricao']} | "
                    f"Status: {chamada['status']}"
                )

    elif opcao == 3:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
