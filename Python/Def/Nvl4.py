def multiplo_fator(a,b):

    if a % b == 0:
        return("É multiplo")
    else:
        return("Não é multiplo") 

a = int(input("Digite um número: "))
b = int(input("Digite seu divisor: "))

print(multiplo_fator(a,b))