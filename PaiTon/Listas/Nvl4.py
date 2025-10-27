#criar lista digitada pelo usuario, cerca de 5 numeros
def criacao():
    lista = []
    for i in range(1,5 + 1):
        num = int(input("Digite um número: "))
        lista.append(num)
    for numero in lista:
        print("Você digitou o número: ", numero)
    return lista
print(criacao())