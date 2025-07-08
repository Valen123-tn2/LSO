n = int(input("Ingrese la cantidad de elementos: "))
a = []

for i in range(n):
    num = int(input("Ingrese los elementos: "))
    a.append(num)

p = 0
for num in a:
    if num % 2 == 0:
        p += 1

print("Cantidad de elementos pares:", p)