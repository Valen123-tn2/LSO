a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
t = 0
if a < 0:
    t = a*b*c
elif a > 0: 
    t = a+b+c

print("El resultado es:",t)