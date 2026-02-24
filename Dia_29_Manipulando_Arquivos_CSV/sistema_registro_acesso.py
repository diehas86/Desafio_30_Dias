acessos = [
    "Diego,15,login",
    "Maria,20,logout",
    "Diego,10,login",
    "Carlos,5,login",
    "Maria,15,login",
    "Carlos,7,logout"
]

dicionario = {}


for item in acessos:
    nome, tempo, status = item.split(",")
    tempo = int(tempo)

    if nome not in dicionario:
        dicionario[nome] = {"login": [], "logout": []}

    dicionario[nome][status].append(tempo)


for usuario, dados in dicionario.items():
    logins = len(dados["login"])
    logouts = len(dados["logout"])
    tempo_total = sum(dados["login"]) + sum(dados["logout"])


    status_final = "ATIVO" if logins > logouts else "INATIVO"
    print("====== Informações do Usuário ======")
    print(f"Usuário: {usuario}")
    print(f"Tempo total: {tempo_total} minutos")
    print(f"Logins: {logins}")
    print(f"Logouts: {logouts}")
    print(f"Status: {status_final}")
    print("------------------------------------")



