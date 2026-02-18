contador_palavras_grandes = 0



frase_usuario = input("Escreva uma frase: ").strip()
if not frase_usuario:
    print("A frase não pode estar vazia ...")



frase_tratada= frase_usuario.translate(str.maketrans("","", ",.;?!/*-+." ))



frase_separada = frase_tratada.split()



for letras in frase_separada:
    if len(letras) >5:
        contador_palavras_grandes = contador_palavras_grandes +1


total_palavras = len(frase_separada)


print(f"Nesse texto existem {total_palavras} palavras ...")
print(f"Existem {contador_palavras_grandes} palavras com mais de cinco letras")

