compras = [
    {"cliente": "Ana", "valor": 150},
    {"cliente": "Carlos", "valor": 200},
    {"cliente": "Maria", "valor": 300},
    {"cliente": "João", "valor": 120},
    {"cliente": "Fernanda", "valor": 450},
    {"cliente": "Lucas", "valor": 80},
    {"cliente": "Beatriz", "valor": 230},
    {"cliente": "Rafael", "valor": 500},
    {"cliente": "Juliana", "valor": 175},
    {"cliente": "Pedro", "valor": 90},

    {"cliente": "Ana", "valor": 220},
    {"cliente": "Carlos", "valor": 130},
    {"cliente": "Maria", "valor": 50},
    {"cliente": "João", "valor": 340},
    {"cliente": "Fernanda", "valor": 120},
    {"cliente": "Lucas", "valor": 410},
    {"cliente": "Beatriz", "valor": 95},
    {"cliente": "Rafael", "valor": 60},
    {"cliente": "Juliana", "valor": 700},
    {"cliente": "Pedro", "valor": 180},

    {"cliente": "Camila", "valor": 260},
    {"cliente": "Bruno", "valor": 310},
    {"cliente": "Patricia", "valor": 140},
    {"cliente": "Gustavo", "valor": 390},
    {"cliente": "Larissa", "valor": 210},
    {"cliente": "Thiago", "valor": 75},
    {"cliente": "Aline", "valor": 430},
    {"cliente": "Rodrigo", "valor": 160},
    {"cliente": "Vanessa", "valor": 280},
    {"cliente": "Eduardo", "valor": 190},

    {"cliente": "Camila", "valor": 320},
    {"cliente": "Bruno", "valor": 110},
    {"cliente": "Patricia", "valor": 450},
    {"cliente": "Gustavo", "valor": 90},
    {"cliente": "Larissa", "valor": 600},
    {"cliente": "Thiago", "valor": 250},
    {"cliente": "Aline", "valor": 130},
    {"cliente": "Rodrigo", "valor": 470},
    {"cliente": "Vanessa", "valor": 85},
    {"cliente": "Eduardo", "valor": 510},

    {"cliente": "Ana", "valor": 90},
    {"cliente": "Carlos", "valor": 420},
    {"cliente": "Maria", "valor": 150},
    {"cliente": "João", "valor": 200},
    {"cliente": "Fernanda", "valor": 310},
    {"cliente": "Lucas", "valor": 145},
    {"cliente": "Beatriz", "valor": 275},
    {"cliente": "Rafael", "valor": 330},
    {"cliente": "Juliana", "valor": 210},
    {"cliente": "Pedro", "valor": 400}
]


def gasto_por_cliente(compras):
    acumulador_gasto ={}
    
    for item in compras:
        nome = item ["cliente"]
        valor_gasto = item ["valor"]
    
        if nome not in acumulador_gasto:
            acumulador_gasto[nome] = valor_gasto
        else:
            acumulador_gasto[nome] += valor_gasto
    
    return acumulador_gasto


def maior_gasto(totais):
    maior_valor = 0
    cliente_maior = ""

    for nome, valor in totais.items():
        if valor > maior_valor:
            maior_valor = valor
            cliente_maior = nome

    return cliente_maior, maior_valor


totais = gasto_por_cliente(compras)
cliente, valor = maior_gasto(totais)

print("Totais por cliente:")
for nome, total in totais.items():
    print(f"{nome}: {total}")

print("\nCliente que mais gastou:")
print(f"{cliente} - {valor}")