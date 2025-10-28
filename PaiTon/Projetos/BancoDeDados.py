#criar um banco de dados aonde o supervisor acrescente uma categoria de funcionarios.
#utilize listas, apenas. Sem tuplas ou dicionarios

Programadores = []

def programadores():
    while True:
        incluir = str(input("Digite o nome do programador: "))
        Programadores.append(incluir)
        escolha = str(input("Deseja encerrar? "))
        if escolha.lower() == "sim":
            chooseBusca = str(input("Deseja fazer alguma consulta? "))
            if chooseBusca.lower() == "sim":
                consulta = str(input("Qual o nome? "))
                for nome in Programadores:
                    encontrado = True
                    if nome == consulta:
                        print ("Incluso!")
                        encontrado = False
                        break
                    if not encontrado:
                        print ("Não encontrado! ")
                solicitacaoLista = str(input("Deseja ver a lista geral? "))
                if solicitacaoLista.lower() == "sim":
                    print (Programadores)
                else:
                    solicitacaoInicio = str(input("Deseja retornar ao inicío? "))
                    if solicitacaoInicio.lower() == "sim":
                        continue
                    else:
                        break
print(programadores())
