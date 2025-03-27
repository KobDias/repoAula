n = int(input("Insere: "))
contador = 1
soma=0
while contador != n+1:
    print(contador, end=", ")
    soma += contador
    contador+=1
    if contador == n+1:
        print(f"\n{soma}")