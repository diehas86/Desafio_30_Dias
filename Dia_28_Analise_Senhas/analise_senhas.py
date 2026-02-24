senhas = [
    "abc12345",
    "senha",
    "12345678",
    "Python2026",
    "abc",
    "segura99"
]

senhas_validas = []
senhas_invalidas = []

for senha in senhas:
    
    tem_numero = False
    
    # Verifica caractere por caractere
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
    
    # Validação final
    if len(senha) >= 8 and tem_numero:
        senhas_validas.append(senha)
    else:
        senhas_invalidas.append(senha)

print(f"Total analisado: {len(senhas)}")
print(f"Senhas válidas: {len(senhas_validas)}")
print(f"Senhas inválidas: {len(senhas_invalidas)}")