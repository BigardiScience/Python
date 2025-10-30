#enumerate() é uma função que permite percorrer uma lista e, ao mesmo tempo, acessar o índice (posição) de cada item.

lista = ["Louveira", "Jundiaí", "Chapecó", "Itatiba", "Vivendas", "Residencial"]

for indice, nome in enumerate(lista,start=1):
    print(f"{indice} : {nome}")