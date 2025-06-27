V = []
for i in range(10):
    valor = int(input("valor {}: ".format(i+1)))
    V.append(valor)

valor11 = int(input("Ingrese valor a insertar: "))
V.append(valor11)

for x in range(11):
    for y in range(10):
        if V[y] > V[x]:
            V[x], V[y] = V[y], V[x]

for x in range(11):
    print(V[x])
