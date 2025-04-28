import math
print("1- Area del triangulo" )
print("2- Area del circulo")
o = int(input("Ingrese la operacion a realizar: "))

if o == 1: 
    lt = float(input("Ingrese el lado del triangulo: "))
    a = ((3**0.5)/4)*lt**2
    print("El area del triangulo es:",a)
elif o == 2: 
    rc = float(input("Ingrese el radio del circulo: "))
    a = math.pi*rc**2
    print("El area del circulo es:", a)