n = int(input("Ingrese la cantidad de elementos en los arreglos: "))
a1 = []
a2 = []
s = []

for i in range(n):
    num = int(input("Elementos del arreglo 1: "))
    a1.append(num)

for i in range(n):
    num = int(input("Elementos del arreglo 2: "))
    a2.append(num)

for i in range(n):
    s.append(a1[i] + a2[i])

print("La suma de los elementos de los dos arreglos es:",s)
