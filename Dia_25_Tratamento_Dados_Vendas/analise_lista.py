lista_geral_vendas = [
    {"produto": "Teclado", "quantidade": 2, "valor_unitario": 150.0},
    {"produto": "Mouse", "quantidade": 5, "valor_unitario": 80.0},
    {"produto": "Monitor", "quantidade": 1, "valor_unitario": 1200.0},
    {"produto": "Teclado", "quantidade": 1, "valor_unitario": 150.0},
    {"produto": "Mouse", "quantidade": 2, "valor_unitario": 80.0},
    {"produto": "Cadeira", "quantidade": 1, "valor_unitario": 900.0}
]

relatorio = {}
faturamento_total_geral = 0 # Inicializando o total geral

# 1. Agrupamento e Soma
for item in lista_geral_vendas:
    nome = item["produto"].lower().strip()
    quantidade = int(item["quantidade"])
    valor_unitario = float(item["valor_unitario"])
    faturamento_item = quantidade * valor_unitario
    
    # Soma ao faturamento global de todos os produtos
    faturamento_total_geral = faturamento_total_geral + faturamento_item

    if nome in relatorio:
        # Se já existe, atualiza os valores
        relatorio[nome]["quantidade_total"] += quantidade
        relatorio[nome]["faturamento_total"] += faturamento_item
    else:
        # Se é novo, cria com nomes de chaves consistentes
        relatorio[nome] = {
            "quantidade_total": quantidade,
            "faturamento_total": faturamento_item
        }

# 2. Identificar Maior e Menor Faturamento
produto_maior = ""
valor_maior = -1.0

produto_menor = ""
valor_menor = -1.0
primeiro_item = True

for nome in relatorio:
    faturamento_atual = relatorio[nome]["faturamento_total"]
    
    # Lógica para Maior
    if faturamento_atual > valor_maior:
        valor_maior = faturamento_atual
        produto_maior = nome
        
    # Lógica para Menor
    if primeiro_item:
        valor_menor = faturamento_atual
        produto_menor = nome
        primeiro_item = False
    else:
        if faturamento_atual < valor_menor:
            valor_menor = faturamento_atual
            produto_menor = nome

# 3. Exibição dos Resultados
print("=== RESUMO POR PRODUTO ===")
for nome in relatorio:
    qtd_total = relatorio[nome]["quantidade_total"]
    fat_prod = relatorio[nome]["faturamento_total"]
    print(f"Produto: {nome.capitalize():<10} | Qtd: {qtd_total:<3} | Faturamento: R$ {fat_prod:>8.2f}")

print("-" * 45)
print(f"Faturamento Total Geral: R$ {faturamento_total_geral:.2f}")
print(f"MAIOR faturamento: {produto_maior.capitalize()} (R$ {valor_maior:.2f})")
print(f"MENOR faturamento: {produto_menor.capitalize()} (R$ {valor_menor:.2f})")

