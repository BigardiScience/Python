lista = []

while True:
    num = int(input("Digite números positivos: "))
    if num >= 0:
        lista.append(num)
    else:
        print("Eu disse Positivos! ")
        break
print(len(lista), "números posítivos foram digitados.")