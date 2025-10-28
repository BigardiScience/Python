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
        for FiltroNome in busca:
            print("Já existente!")
            encontradoNome = True
            break
        if not FiltroNome in busca:
            print("Não Encontrado.")
            break
    elif processoFiltro.lower() == "idade":
        FiltroIdade = int(input("Digite a idade: "))
        encontradoIdade = False
        for FiltroIdade in busca:
            print("Já existente!")
            encontradoIdade = True
            break
        if not FiltroIdade in busca:
            print("Não Encontrado.")
            break
    elif processoFiltro.lower() == "cidade":
        FiltroCidade = input("Digite a cidade: ")
        encontradoCidade = False
        for filtroCidade in busca:
            print("Já existente")
            encontradoCidade = True
            break
        if not filtroCidade in busca:
            print("Não Encontrado.")
            break
