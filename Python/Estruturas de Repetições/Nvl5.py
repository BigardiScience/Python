listaGasto = []

while True:
    consumo = int(input("Digite seus gastos: "))
    escolha = input("Houve mais gastos? ")
    if escolha.lower() == "sim" :
        listaGasto.append(consumo)
    else:
        print(listaGasto)
        break
print("Você acrescentou: ",len(listaGasto),"gastos" " e seu gasto total foi de: ",sum(listaGasto))