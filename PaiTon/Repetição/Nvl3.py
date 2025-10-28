lista = []
while True:
    nome = input("Acrescente nomes, mas caso queira parar, digite 'sair': ")
    if nome == "sair":
        print("Encerrado")
        break
    else:
        lista.append(nome)

print(lista)
