tc = float(input("Ingrese el total de la cuenta: "))
p = float(input("Ingrese el porcentaje de propina que quiere dejar: "))
t = 0
p = tc*(p/100)
t = tc + p

print("El total a pagar es:",t)
