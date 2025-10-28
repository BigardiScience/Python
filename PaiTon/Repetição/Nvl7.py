listaGastos = []

while True:
    gastos = int(input("Digite seus gastos: "))
    choose = input("Quer finalizar? ")
    if choose != "sim":
        listaGastos.append(gastos)
    else:
        listaGastos.append(gastos)
        print("Gastos Totais: ", sum(listaGastos))
        print("Valores Únicos: ", sum(set(listaGastos)))
        print("Quantidade de Gastos: ", len(listaGastos))
        media = sum(listaGastos) / len(listaGastos)
        print("Média de Gastos", round(media,2))
        print("Maior Número: ", max(listaGastos))
        print("Menor Número: ", min(listaGastos))
        break