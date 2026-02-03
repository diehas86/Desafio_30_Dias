#===================================#
#======= calculadora simples =======#
#===================================#


numero_1 = float(input("Digite o primeiro número que deseja realizar a conta: "))
numero_2 = float(input("Digite o segundo número que deseja realizar a conta: "))

soma = (numero_1 + numero_2)
subtracao = (numero_1 - numero_2)
multiplicacao = (numero_1 * numero_2)

print("============= calculando... ===============")
print(f"O resultado da soma dos números é : {soma:.2f}")
print(f"O resultado da subtração dos numeros é: {subtracao:.2f}")
print(f"O resultado da multiplicação dos numeros é: {multiplicacao:.2f}")