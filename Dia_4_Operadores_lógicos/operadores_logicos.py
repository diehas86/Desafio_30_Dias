idade = int(input("Digite sua idade: "))
cadastro = input("Você possui cadastro? (Sim/Não) ")
termos_uso = input("Aceita os termos de uso do programa? (Sim/Não) ") 


if idade < 18 or cadastro == ("Não") or termos_uso == ("Não"):
    print ("Você não preenche os requisitos mínimos para acessar o programa...")

else:
    print("Usuário cadastrado com sucesso...") 