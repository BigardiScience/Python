dados = []

while True:
    nome = input("Digite o nome para cadastro: ")
    idade = int(input("Digite a idade: "))
    cargo = input("Cargo: ")
    dados.append((nome,idade,cargo))
    print(f"O {nome} com {idade} anos de idade foi cadastrado no cargo de {cargo}")
    choose = input(f"Deseja continuar cadastrando? ")
    if choose.lower() != "sim":
        break

for busca in dados:
    nome = busca[0]
    idade = busca[1]
    cargo = busca[2]
    print(f"Cadastrado: {nome} : {idade} : {cargo}")
