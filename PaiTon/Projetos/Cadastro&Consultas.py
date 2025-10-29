dados = []
def cadastro():
    while True:
        nome = input("Digite o nome para cadastro: ")
        idade = int(input("Digite a idade: "))
        cargo = input("Cargo: ")
        dados.append((nome,idade,cargo))
        print(f"O {nome} com {idade} anos de idade foi cadastrado no cargo de {cargo}")
        choose = input(f"Deseja continuar cadastrando? ")
        if choose.lower() != "sim":
            break
    return f"Visão Geral : {dados}"
print(cadastro())

for indice, busca in enumerate(dados, start=1):
    nome = busca[0]
    idade = busca[1]
    cargo = busca[2]
    print(f"{indice} - {nome} , {idade} , {cargo}")
    opcaoInicio = input(f"Deseja retornar ao inicio? ")
    if opcaoInicio.lower() != "sim":
        print("Fim do Programa! ")
        break
    else:
        print(cadastro())
    #esse exercício achei deveras interessante por ter sido feito, conforme o restante, de forma independente aplicando apenas o conhecimento obtido
