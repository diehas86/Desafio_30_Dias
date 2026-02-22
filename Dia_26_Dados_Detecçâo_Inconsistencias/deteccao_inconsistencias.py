total_validos=[]
total_invalidos=[]

usuarios = [
    {"nome": "Ana", "idade": 25, "email": "ana@gmail.com", "ativo": True},
    {"nome": "Bruno", "idade": -5, "email": "bruno@gmail.com", "ativo": True},
    {"nome": "Carlos", "idade": 130, "email": "carlos@gmail.com", "ativo": False},
    {"nome": "Daniela", "idade": 30, "email": "danielaemail.com", "ativo": True},
    {"nome": "Eduardo", "idade": 45, "email": "eduardo@gmail.com", "ativo": False},
    {"nome": "Fernanda", "idade": 22, "email": "fernanda@", "ativo": True},
    {"nome": "Gabriel", "idade": 0, "email": "gabriel@gmail.com", "ativo": True},
    {"nome": "Helena", "idade": 120, "email": "helena@gmail.com", "ativo": True},
    {"nome": "Igor", "idade": 28, "email": "", "ativo": False},
    {"nome": "Juliana", "idade": 35, "email": "juliana@gmail.com", "ativo": True}
]

for usuario in usuarios:
    nome = usuario ["nome"]
    idade = usuario ["idade"]
    email = usuario["email"]
    ativo = usuario ["ativo"]

    valido = True

    if not nome.strip() or len(nome)<2:
        valido = False

    if idade < 0 or idade > 120:
        valido = False

    if "@" not in email or "." not in email:
        valido = False
    
    if ativo is not True:
        valido = False 
    
    
    if valido:
        total_validos.append(usuario)
    else:
        total_invalidos.append(usuario)


print("-----Resumo geral-----")
print(f"O numero de usuários total são {len(usuarios)} usuários")
print(f"O numero total de usuarios válidos são {len(total_validos)}")
print(f"O número total de usuários inválidos são {len(total_invalidos)}")
