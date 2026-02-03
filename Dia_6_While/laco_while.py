senha = int(1234)
numero_tentativas= int(3)

while numero_tentativas > 0:
    
    senha_do_usuario = int(input("Digite a senha do usuário: "))
    
    
    if senha_do_usuario == senha:
        print("Acesso permitido...")
        numero_tentativas == 0    #can`t use break so i use == 0 to force stop 

    
    else:
        numero_tentativas -= 1
        if numero_tentativas > 0:
            print(f"Senha incorreta você tem mais {numero_tentativas} chances...")
        else:
            print("Suas tentativas se esgotaram ...")

print("Fim do programa...")




