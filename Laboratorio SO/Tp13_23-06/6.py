V1 = []
n = int(input("Ingrese cantidad de elementos del vector: "))

for x in range(n):
    valor = int(input("V{}: ".format(x+1)))
    V1.append(valor)

for y in range(n):
    for x in range(n-1):
        if V1[x] < V1[x+1]:
            V1[x], V1[x+1] = V1[x+1], V1[x]

print(V1)
