def checar(a):
    if a % 3 == 0:
        print(a," é múltiplo de 3.")
    else:
        print(a," não é múltiplo de 3.")
    
    

a = int(input("Digite um número: "))

print(checar(a))