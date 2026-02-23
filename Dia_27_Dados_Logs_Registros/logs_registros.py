registros_acesso = [
    "ana,success",
    "joao,fail",
    "ana,fail",
    "maria,success",
    "joao,success",
    "ana,success",
    "maria,fail",
    "joao,fail",
    "ana,success"
]

contagem_acessos={}
acesso_success = []
acesso_fail = []

for registro in registros_acesso:
    usuario , status = registro.split(",")

    if usuario in contagem_acessos:
        contagem_acessos[usuario] += 1
    elif usuario not in contagem_acessos:
        contagem_acessos [usuario] = 1 
    
    if status == "fail":
        registro = False
        acesso_fail.append(usuario)
    else:
        acesso_success.append(usuario)

print(f"O total de acessos bem sucedidos foram {len(acesso_success)} acessos.")
print(f"O total de acessos que falharam foram {len(acesso_fail)} acessos.")

print ("Número de acesso por usuários: ")
for usuario, total in contagem_acessos.items():
    print(f"{usuario}: {total}")



