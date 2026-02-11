def validar_nome(nome):
    sem_espaco = nome.strip()
    if sem_espaco == "":
        return False

    if len(sem_espaco) <4:
        return False
    for letra in sem_espaco:
        if not letra.isalpha() and letra != " ":
            return False
    return True


def validar_idade(idade):
    if not idade.isdigit():
        return False
    idade = int(idade)
    if idade<18:
        return False
    return True

def validar_email (email):
    email = email.strip()
    if len(email) < 5:
        return False
    if "@" not in email or "." not in email:
        return False
    if " " in email:
        return False
    return True


def validar_senha (senha):
    senha = senha.strip()
    tem_letra = False
    tem_numero = False
    if len (senha) < 6:
        return False
    for caractere in senha:
        if caractere.isalpha():
            tem_letra = True
        elif caractere.isdigit():
            tem_numero = True
    if not tem_letra or not tem_numero:
        return False
    return True
    
nome = input("Digite o nome para cadastro: ")
while not validar_nome(nome):
    print("Nome inválido tente novamente...")
    nome = input("Digite o nome para cadastro: ")
print("Nome válido", nome)



idade = input("Digite a idade para cadastro: ")
while not validar_idade(idade):
    print("idadae incorreta tente novamente...")
    idade = input("Digite a idade para cadastro: ")
print("Idade válida", idade)



email = input("Digite o email para cadastro: ")
while not validar_email(email):
    print("email incorreto, tente novamente...")
    email = input("Digite o email para cadastro: ")
print("Email correto", email)


senha =input("Digite a senha para cadastro: ")
while not validar_senha(senha):
    print("senha inválida tente novamente ...")
    senha =input("Digite a senha para cadastro: ")
print("Senha válida", senha)


print ("Cadastro realizado com sucasso!")
    