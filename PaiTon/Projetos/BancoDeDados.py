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
                    if nome == consulta:
                        return "Incluso!"
                    else:
                        print ("Não encontrado! ")
            else:
                escolhaVisaoGeral = str(input("Deseja ver toda a lista? "))
                if escolhaVisaoGeral.lower() == "sim":
                    return Programadores
                else:
                    print("Fim do Programa")
                    break


print(programadores())