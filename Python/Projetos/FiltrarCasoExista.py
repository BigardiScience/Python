#Criar um programa que filtre e identifique se tal informação já se encontra no banco


alunoS = [("Guilherme", 21, "Jundiaí"),
         ("Pedro", 16, "Jundiaí"),
         ("Heitor", 16, "Louveira")]

for busca in alunoS:
    nome = busca[0]
    idade = busca[1]
    cidade = busca[2]
    processoFiltro = str(input("Deseja filtrar por nome, idade, ou cidade? "))
    if processoFiltro.lower() == "nome":
        FiltroNome = str(input("Digite o Nome: "))
        encontradoNome = False
        if FiltroNome in busca:
            print("Já existente!")
            encontradoNome = True
            break
        if not FiltroNome in busca:
            print("Não Encontrado.")
            break
    elif processoFiltro.lower() == "idade":
        FiltroIdade = int(input("Digite a idade: "))
        encontradoIdade = False
        if FiltroIdade in busca:
            print("Já existente!")
            encontradoIdade = True
            break
        if not FiltroIdade in busca:
            print("Não Encontrado.")
            break
    elif processoFiltro.lower() == "cidade":
        FiltroCidade = input("Digite a cidade: ")
        encontradoCidade = False
        if filtroCidade in busca:
            print("Já existente")
            encontradoCidade = True
            break
        if not filtroCidade in busca:
            print("Não Encontrado.")

            break
