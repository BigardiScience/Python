cartao = int(input("Digite o número do seu cartão: "))                  
debitos = int(input("Quantos débitos seram realizados? "))
lista = []
cartoes = []
soma = 0
limite = int(input("Qual o limite do seu cartão? "))
cartoes.append(cartao)



for i in range(1,debitos+1):
    gasto = float(input("Qual o valor? "))
    soma += gasto
    lista.append(gasto)
    RestoLimite = limite - soma

if limite > soma :
    print("Você ainda há limite")
else:
    print("Limite ultrapassado!")

solicitacao = str(input("Você deseja ver seus cartões cadastrados?  S/N     "))
if solicitacao.upper() == "S":
    print("Cartões cadastrados: ",cartao)

    restante = str(input("Quer visualizar quanto de limite ainda falta?  S/N        "))
    if restante.upper() == "S":
        print("Restam: R$",RestoLimite,"REAIS")
else:
    print("Até a próxima!")

    
total = sum(lista)
print("GASTO GERAL: R$",total,"REAIS")