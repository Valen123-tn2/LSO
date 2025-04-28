a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

d = b**2-4*a*c

if d > 0:
    x1 = ((-b) + d**0.5)/2*a
    x2 = ((-b) + d**0.5)/2*a
    print("Raices reales: ",x1,x2)
else: 
    print("Raices irracionales")
