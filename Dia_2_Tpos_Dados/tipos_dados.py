#===================================#
#========= Tipos de Dados ==========#
#===================================#

nome = input("Digite seu nome: ").strip()
print (f"O nome é do tipo : {type(nome)}")
idade = int(input("Digite sua idade: "))
print (f"A idade é do tipo :{type(idade)}")
altura = float(input("Digite sua altura: "))
print (f"A altura é do tipo{type(altura)}")
emprego = input("Esta empregado? (responda apenas com Sim ou Não) ").strip()
resultado_emprego = emprego == "sim"
print(f"O emprego é do tipo: {type(resultado_emprego)}")


print("=========== RESUMO ============")
print(f"O nome inserido é : {nome}...")
print(f"A idade inserida é : {idade}...")
print(f"A altura inserida é :{altura}...")
print(f"Está empregado : {'Sim' if resultado_emprego else 'Não'}")

