vendas_diarias = [300, 250, 400, 150, 100, 500]
soma_total = 0
maior_venda = vendas_diarias[0]
menor_venda = vendas_diarias[0]
acima_media=[]

#   Maior Venda
for venda in vendas_diarias:
    if venda > maior_venda:
        maior_venda = venda

#   Menor Venda
for venda in vendas_diarias:
    if venda < menor_venda:
        menor_venda = venda
       
#   Dias Trabalhados
dias_trabalhados = len(vendas_diarias)

#   Valor Total 
for soma in vendas_diarias:
    soma_total += soma

#   Média de Vendas
media_vendas = soma_total/dias_trabalhados



#   Vendas Acima da média
for venda in vendas_diarias:
    if venda > media_vendas:
        acima_media.append(venda) 





print("======================== Dados Tratados ============================")
print(f"O total de dias da semana trabalhados são: {dias_trabalhados} dias.")
print("--------------------------------------------------------------------")
print(f"A soma total vendida na semana é : R${soma_total:.2f}")
print("--------------------------------------------------------------------")
print(f"A maior venda da semana foi: R${maior_venda:.2f}")
print("--------------------------------------------------------------------")
print(f"A menor venda da semana foi: R${menor_venda:.2f}")
print("--------------------------------------------------------------------")
print(f"A média de vendas foi: R${media_vendas:.2f}")
print("--------------------------------------------------------------------")
print(f"A quantidade dias com vendas acima da média foram: {len(acima_media)}")
print("--------------------------------------------------------------------")

