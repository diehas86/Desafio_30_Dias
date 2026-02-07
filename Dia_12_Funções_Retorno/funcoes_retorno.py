todas_notas = []



def informe_notas():
    nota = float(input("Digite a nota do aluno: "))
    if nota  < 0 or nota>10:
        print("Nota inválida , digite uma nota entre 0 á 10")
        return None
    
    else:
        print("Nota adicionada com sucesso...")
        todas_notas.append(nota)
        return nota

def media():
    if not todas_notas:
        print("Nenhuma nota registrada...")
        return
    else:
        media_atual = sum(todas_notas) / len(todas_notas)
        print(f" A media do aluno é {media_atual}")
        return media_atual
        


def aprovacao(resultado_media):
    if resultado_media < 7:
        print("Aluno reprovado...")
    else:
        print("Aluno aprovado...")
 

# resultado_media=media()


while True:
    print("===== Menu =====")
    print("1-Informar as notas")
    print("2-Obter média")
    print("3-Obter resultado")
    print("4-  Sair")
    opcao = int(input("Digite a opção numérica  do menu: "))

    if opcao <1 or opcao >4:
        print("Digite apenas um número válido")

    elif opcao == 1:
        informe_notas()
        

    elif opcao == 2:
        media()
        

    elif opcao == 3:
        resultado_media = media()
        if resultado_media is not None:
            aprovacao(resultado_media)
    
    elif opcao == 4:
        print("Saindo do sistema...")
        break















