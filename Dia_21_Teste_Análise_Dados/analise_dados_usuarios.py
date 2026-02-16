while True:
    texto = input("Digite um texto a seguir: ").strip()

    if not texto:
        print ("O texto não pode estar vazio...")
    else:
        break

texto_limpo = texto.translate(str.maketrans("","",".,;?!"))

palavras = texto_limpo.split() 


maior_palavra = palavras[0]
menor_palavra = palavras[0]



for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    if len (palavra) < len(menor_palavra):
        menor_palavra = palavra



print(f"O texto tem {len(palavras)} palavras.")
print(f"A maior palavra do texto é: {maior_palavra}")
print(f"A menor palavra do texto é: {menor_palavra}")



