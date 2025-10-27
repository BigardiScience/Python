def checar(a):
    if a % 2 == 0: ## se 'a' o resto da divisao por 2 for igual a zero, é par
        print("Par")
    else:
        print("Impar")

    return a

a = int(input("Digite um número para análise: "))

print(checar(a))



    