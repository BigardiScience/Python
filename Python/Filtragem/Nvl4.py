lista = [()]

while True:
    solicitacao = input(f"Digite nome: ")
    idade = int(input(f"Digite a idade: "))
    lista.append((solicitacao,idade))
    break
for i, nome in enumerate(lista,start=1):
    print(f"{i} - O {solicitacao} tem {idade} anos de idade ")
    break