n = int(input("Ingrese la cantidad de elementos: "))
a = []

for i in range(n):
    num = int(input("Ingrese los elementos: "))
    a.append(num)

print("Elementos únicos:")
for num in a:
    if a.count(num) == 1:
        print(num)