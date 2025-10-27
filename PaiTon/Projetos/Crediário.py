#Registo de Cartões de crediário 

cartao = int(input("Digite o número do seu cartão: "))
lista = []
quantidade = int(input("Quantos pagamentos deseja realizar? "))
soma = 0
for i in range(1, quantidade+1):
    valores = int(input("Qual o valor do débito? "))
    soma += valores
somatotal = soma

limite = int(input("Qual o limite do seu cartão esse mês? "))
if somatotal > limite:
    print("Limite Excedido!")
else:
    calculo = limite - somatotal  
    print("Restam: R$",calculo," reais")
lista.append (cartao)

solicitacao = input("Quer acessar seus registros de cartões? [S],[N]: ")
if solicitacao.upper() == "S":
    print(lista)
else:
    print("Até a próxima!")
