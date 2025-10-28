# Criar um banco de dados onde o supervisor acrescente uma categoria de funcionários.
# Utilizando apenas listas, sem tuplas ou dicionários.

Programadores = []

def programadores():
    while True:
        incluir = input("Digite o nome do programador: ")
        Programadores.append(incluir)

        escolha = input("Deseja encerrar? ")
        if escolha.lower() == "sim":
            chooseBusca = input("Deseja fazer alguma consulta? ")
            if chooseBusca.lower() == "sim":
                consulta = input("Qual o nome? ")
                encontrado = False
                for nome in Programadores:
                    if nome == consulta:
                        print("Incluso!")
                        encontrado = True
                        break
                if not encontrado:
                    print("Não encontrado!")

            solicitacaoLista = input("Deseja ver a lista geral? ")
            if solicitacaoLista.lower() == "sim":
                print("Lista de programadores:", Programadores)

            solicitacaoInicio = input("Deseja retornar ao início? ")
            if solicitacaoInicio.lower() == "sim":
                continue
            else:
                return "Fim do Programa"

print(programadores())