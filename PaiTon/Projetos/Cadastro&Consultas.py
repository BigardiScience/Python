funcionarios = []

while True:
    #entrada de dados cadastro in tupla
    solicitacao = input("Digite um nome: ")
    idade = int(input("Digite a idade: "))
    funcionarios.append((solicitacao,idade))
    continuar = input(f"Deseja continuar cadastrando? ")
    if continuar.lower() != "sim":
        filtragem = input(f"Deseja filtrar algum dos dados? ")
        if filtragem.lower() == "sim":
            filtro = input(f"Por nome ou idade? ")
            if filtro.lower() == "nome":
                filtroNome = input("Qual o nome? ")
                encontrado = False
                for i, busca in enumerate(funcionarios,start=1):
                    if busca[0] == filtroNome:
                        print(f"Funcionário encontrado na posição {i} : {busca}")
                        encontrado = True
                        break
                if not encontrado:
                        print("Não Encontrado!")
            elif filtro.lower() == "idade":
                filtroIdade = int(input("Qual a idade? "))
                encontradoIdade = False
                for i, dataNascimento in enumerate(funcionarios,start=1):
                    if dataNascimento[1] == filtroIdade:
                        print(f"Funcionário encontrado na posição {i} : {dataNascimento}")
                        encontradoIdade = True
                        break
                if not encontradoIdade:
                    print("Não Encontrado!")
        inicio = input("Deseja Voltar ao cadastro? ")
        if inicio.lower() != "sim":
            print("Até a Próxima!")
            break


        

