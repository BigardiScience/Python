#enumerate() é uma função que permite percorrer uma lista e, ao mesmo tempo, acessar o índice (posição) de cada item.

lista = ["Louveira", "Jundiaí", "Chapecó", "Itatiba", "Vivendas", "Residencial"]

for indice, nome in enumerate(lista):
    print(f"{indice} : {nome}")
