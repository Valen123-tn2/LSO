n = int(input("Ingrese la cantidad de elementos: "))
a = []

for i in range(n):
    num = int(input("Ingrese los elementos: "))
    a.append(num)


print("Arreglo invertido:")
print(a[::-1])