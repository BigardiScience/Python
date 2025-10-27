solicitado = int(input("Quantas contas deseja calcular? "))
soma = 0

for i in range(1, solicitado+1):
    num = int(input("Digite o valor: "))
    soma += num

SomaTotal = soma

LimiteCartao = float(input("Qual seu limite do cartão? "))

if SomaTotal > LimiteCartao:
    print("Cartão estourado!")
else:
    print("Dentro dos limites!")