s = 20000
r = int(input("Ingrese el monto a retirar: "))
if r > s: 
    print("Saldo insuficiente")
else:
    s = s-r
    print("Su saldo restantre es de",s)