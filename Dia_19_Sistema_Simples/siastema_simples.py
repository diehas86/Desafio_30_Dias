def menu_principal():
    print("1 - Horários de funcionamento.")
    print("2 - Falar com atendente.")
    print("3 - Encerrar atendimento.")
    opcao = input("Digite a opção numérica desejada: ").strip()

    if not opcao:
        print("Ops parece que você não escreveu nada, por favor digite uma opção válida (1,2,3).")
        return None
    if not opcao.isdigit():
        print("Por favor digite apenas números validos (1,2,3).")
        return False
    opcao = int(opcao)
    if opcao <1 or opcao >3:
        print("Apenas numeros entre (1,2,3) serão aceitos")
        return False

    return opcao

    
while True:
    
    opcao=menu_principal()

    if opcao is None:
        continue

    if opcao == 1:
        print("Horario de funcionamento")
        print("De segunda a sexta")
        print("De 9:00 às 17:00 ")
    
    
    elif opcao == 2:
        print("Em breve um atendente entrará em contato com você...")
    
    
    elif opcao == 3:
        print("Encerrando atendimento...")
        break
    

    
