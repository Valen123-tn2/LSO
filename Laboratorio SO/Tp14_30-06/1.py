n = int(input("Ingrese la cantidad de elementos: "))
a = []

for i in range(n):
    num = int(input("Ingrese el elemento: "))
    a.append(num)

p = 1
for num in a:
    p *= num

print("Producto de todos los elementos:", p)