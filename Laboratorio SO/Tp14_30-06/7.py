n = int(input("Ingrese la cantidad de elementos: "))
a = []

for i in range(n):
    num = int(input("Ingrese los elementos: "))
    a.append(num)

b = int(input("Número a buscar: "))

if b in a:
    print("El número está presente en el arreglo.")
else:
    print("El número no está en el arreglo.")