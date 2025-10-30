lista = []

while True:
    num = int(input("Digite um número positivo: "))
    if num >= 0:
        lista.append(num)
    else:
        print("Eu disse POSITIVO!")
        break
print("Quantidade Positivos: ", len(lista))
print("Soma Total: ", sum(set(lista)))
media = sum(lista) / len(lista)
print("Média Geral: ", round(media,2))