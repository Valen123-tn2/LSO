n = int(input("Ingrese dimensión del vector: "))
v = n*['']
for i in range(n):
    v[i] = input("Ingrese Caracter: ")

d = n
for i in range(n//2):
    v[i], v[d-1] = v[d-1], v[i]
    d -= 1

for i in range(n):
    print(v[i])
