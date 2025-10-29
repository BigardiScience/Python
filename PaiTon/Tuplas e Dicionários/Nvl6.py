#Modelo Iniciante seus arrombados
dados = []

while True:
    nome = input("Digite o nome para cadastro: ")
    idade = int(input("Digite a idade: "))
    cargo = input("Cargo: ")
    dados.append((nome,idade,cargo)) #um ponto interessante é que aqui adicionamos TUPLAS("Lista" que não podem ser alterada), dentro de uma lista.
    print(f"O {nome} com {idade} anos de idade foi cadastrado no cargo de {cargo}")
    choose = input(f"Deseja continuar cadastrando? ")
    if choose.lower() != "sim":
        break

for busca in dados:
    nome = busca[0]
    idade = busca[1]
    cargo = busca[2]
    print(f"Cadastrado: {nome} : {idade} : {cargo}")



#Esse modelo abaixo é mais avançado
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
    

