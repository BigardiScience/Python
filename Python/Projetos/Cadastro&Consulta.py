lista = []
while True:
    pergunta = input("Deseja se cadastrar ou sair? ")
    if pergunta.lower() == "cadastrar":
        pergunta_nome = input("Digite um nome: ")
        pergunta_idade = int(input("Digite a idade: "))
        lista.append((pergunta_nome, pergunta_idade))
        pergunta_filtro = input("Deseja filtrar? ")
        pergunta_multipla = input("Por nome ou idade?")
        if pergunta_multipla.lower() == "nome":
            filtro_nome = input("Digite o nome para filtrar: ")
            encontrado = False
            for busca in lista:
                if filtro_nome.lower() == busca[0].lower():
                    print("Encontrado! ")
                    encontrado = True
                    break
        elif pergunta_multipla.lower() == "idade":
            filtro_idade = int(input("Digite a idade para filtrar: "))
            encontrado = False
            for busca in lista:
                if filtro_idade == busca[1]:
                    print("Encontrado! ")
                    encontrado = True
                    break
            if not encontrado:
                print("Não Encontrado. ")           

        pergunta_final = input("Deseja voltar ao cadastro? ")
        if pergunta_final.lower() != "sim":
            pergunta_visualizar = input("Quer visualizar lista? ")
            if pergunta_visualizar.lower() == "sim":
                print(lista)
            else:
                print("Fim do programa! ")
            break
    elif pergunta.lower() == "sair":
        print("Fim do Programa. ")
        break
