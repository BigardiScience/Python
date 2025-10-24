lista = []
num = int(input("Quantos itens quer cadastrar? "))

for i in range(1,num + 1):
    Itens = str(input("Qual o nome do item? "))
    lista.append ([Itens])

print(lista)