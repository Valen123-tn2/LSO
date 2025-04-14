import math
""" 1 """
"""r = float(input("Ingrese el radio del circulo: "))
p = 3.1416
v = 4/3*p*r**3
print("El volumen es: ",v)"""

""" 2 """
"""h= float(input("Ingrese la altura del triangulo: "))
p = 3*(2*h)/3**0.5
print("El perimetro del triangulo es de: ",p)"""

""" 3 """
"""eu = 3.84
do = 2.28
s = float(input("Ingrese el numero de soles: "))
e = s/eu
d = s/do

print(s,"soles son:",e,"euros y ",d,"dolares")"""

""" 4 """
"""t = float(input("Ingrese el tiempo en segundos: "))
d = float(input("Ingrese los metros: "))
v= d/t
print("La velocidad es de ",v,"m/s")"""

""" 5 """
"""p = float(input("Ingrese el precio del producto: "))
d = float(input("Ingrese la cantidad de docenas a llevar: "))
t = d*12*p
print("El total a pagar es de: ",t)"""

""" 6 """
"""m = float(input("Ingrese las millas: "))
mi = 1.609344
k = m*mi
print(m,"Millas son ",k,"Kilometros")"""

""" 7 """
"""b = float(input("Ingrese la longitud de uno de los lados: "))
c = float(input("Ingrese la longitud de otro de los lados: "))
an = float(input("Ingrese el angulo en grados sexagecimales: "))
a = (b**2 + c**2 - 2*b*c*math.cos(an*math.pi/180))**0.50
print("El tercer lado es de:",a)"""

""" 8 """
"""va = float(input("Ingrese la velocidad del primer cuerpo: "))
vb = float(input("Ingrese la velocidad del segundo cuerpo: "))
d = float(input("Ingrese la distancia entre ellos: "))
t = d/(va+vb)
print("los cuerpos se van a encontrar en ",t,"segundos")"""

""" 9 """
"""ar = float(input("Ingrese el angulo en radianes: "))
asex = ar*180/math.pi
acen = ar*200/math.pi
print("El angulo",ar,"en radianes es",asex,"en sexagesimales y ",acen,"en Centesimales")"""

""" 10 """
"""print("Ingrese los valores de los puntos x1,y1 y z1")
x1 = float(input("x1:"))
y1 = float(input("y1:"))
z1= float(input("z1:"))
print("Ingrese los valores de los puntos x2,y2 y z2")
x2 = float(input("x2:"))
y2 = float(input("y2:"))
z2 = float(input("z2:")) 
d = ((z2-z1)**2 +(y2-y1)**2 + (x1-x2)**2)**0.5
print("La distancia es de: ",d)"""
