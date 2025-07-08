n = int(input("Ingrese la cantidad de elementos: "))
a = []
ao = []

for i in range(n):
    num = int(input("Ingrese los elementos: "))
    a.append(num)
    ao.append(num)
ao.sort()

if a==ao:
        print("El arreglo esta ordenado")
else:
        print("El arreglo no esta ordenado")