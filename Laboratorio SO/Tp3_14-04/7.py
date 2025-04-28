import math
b = float(input("Ingrese la longitud de uno de los lados: "))
c = float(input("Ingrese la longitud de otro de los lados: "))
an = float(input("Ingrese el angulo en grados sexagecimales: "))
a = (b**2 + c**2 - 2*b*c*math.cos(an*math.pi/180))**0.50
print("El tercer lado es de:",a)