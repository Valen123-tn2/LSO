pi = 3.1416
r = float(input("Ingrese el radio del cilindro: "))
a = float(input("ingrese el alto del cilindro: "))

ar = 2*pi*r*(r+a)
v = pi*r**2*a

print("el area del cilindro es",ar," y su volumen es",v)