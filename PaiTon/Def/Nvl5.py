def banco():
    programadores = []
    while True:
        acrescentar = str(input("Acrescente os encarregados: "))
        programadores.append(acrescentar)
        choose = (str(input("Deseja Finalizar? ")))
        if choose.lower() == "sim":
            break
    return (programadores)
    
print(banco())