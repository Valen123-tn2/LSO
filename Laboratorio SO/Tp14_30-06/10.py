n1 = int(input("Ingrese la cantidad de elementos del primer arreglo: "))
a1 = []
for i in range(n1):
    num = int(input("Elementos del primer arreglo: "))
    a1.append(num)

n2 = int(input("Ingrese la cantidad de elementos del segundo arreglo: "))
a2 = []
for i in range(n2):
    num = int(input("Elementos del segundo arreglo: "))
    a2.append(num)

com = a1 + a2

print("Arreglo combinado:",com)
