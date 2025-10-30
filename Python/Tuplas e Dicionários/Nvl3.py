lista = [("Maca", 8,2),
         ("Pêra",5,8),
         ("Banana",10,5)]

for produto in lista: #“Percorra cada item da lista, um por um, e chame esse item dentro de cada tupla de numero enquanto estiver dentro do laço.”
    nome = produto[0]
    preco = produto[1]
    quantidade = produto[2]
    print(f"O produto {nome} custa R${preco} e há {quantidade} disponíveis em estoque.")