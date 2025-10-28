def Calculos_multiplos():
    lista = []
    contador = 0
    num = int(input("Digite um número: "))
    for i in range(1,num + 1):
        lista.append(i)
    print(lista)
    for numero in lista:
        if numero % 5 == 0:
            contador += 1
            print("Há ",contador," multiplos de 5.")
    return(contador)

print(Calculos_multiplos())
        