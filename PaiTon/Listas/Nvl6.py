def filtragem():
    lista = []
    listaMaiores = []
    limite = int(input("Informe até qual número: "))
    for i in range(1,limite + 1):
        num = int(input("Digite a quantidade de números preenchida: "))
        lista.append(num)
    for numero in lista:
        if numero > 10:
            listaMaiores.append(numero)
    return listaMaiores
    
print(filtragem())