n = int(input("Ingrese la cantidad de elementos: "))
a = []

for i in range(n):
    num = int(input("Ingrese los elementos: "))
    a.append(num)

sd = []

for num in a:
    if num not in sd:
        sd.append(num)

print("Arreglo sin duplicados:")
print(sd)