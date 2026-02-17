# Sistema de registro de vendas

total_vendas = []
maior_venda = None
menor_venda = None
valor_total = 0

while True:
    valor_venda = input("Digite o valor de venda (ou Enter para sair): ")

    # Encerrar se o usuário não digitar nada
    if not valor_venda:
        print("Encerrando registro de vendas...")
        break

    # Substitui vírgula por ponto e converte para float
    valor_venda = float(valor_venda.replace(",", "."))

    # Atualiza maior e menor venda
    if maior_venda is None or valor_venda > maior_venda:
        maior_venda = valor_venda
    if menor_venda is None or valor_venda < menor_venda:
        menor_venda = valor_venda

    # Adiciona venda à lista e soma ao total
    total_vendas.append(valor_venda)
    valor_total += valor_venda

    # Pergunta se deseja continuar
    continuar = input("Deseja continuar a cadastrar (s/n)? ")
    if continuar.lower() == "n":
        break

# Calcula média e vendas acima da média
media_vendas = valor_total / len(total_vendas)
vendas_acima_media = [vendas for vendas in total_vendas if vendas > media_vendas]

# Exibe resultados
print("\n--- RESULTADOS ---")
print(f"Total de vendas registradas: {len(total_vendas)}")
print(f"Valor total vendido: {valor_total:.2f}")
print(f"Valor médio das vendas: {media_vendas:.2f}")
print(f"Maior venda: {maior_venda:.2f}")
print(f"Menor venda: {menor_venda:.2f}")
print(f"Quantidade de vendas acima da média: {len(vendas_acima_media)}")
print("Vendas acima da média:")
for vendas in vendas_acima_media:
    print(f"- {vendas:.2f}")

