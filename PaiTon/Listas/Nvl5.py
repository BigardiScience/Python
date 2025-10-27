def criacao():
    lista = []
    for i in range(1,5 + 1):
        num = int(input("Digite números inteiros: "))
        lista.append(num)
    pesquisa = int(input("Digite um número para busca: "))
    if pesquisa in lista:
        return("Número Encontrado! ")
    else:
        return("Número Não Encontrado! ")
     

print(criacao())