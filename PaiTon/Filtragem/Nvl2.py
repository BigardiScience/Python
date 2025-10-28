
lista = []

while True:
    num = int(input("Acrescente as idades: "))
    lista.append(num)
    escolha = input("Deseja continuar? ")
    if escolha.lower() != "sim":
        break

for idade in lista:
    if idade <18:
        print("Idade dos menores:",idade)
