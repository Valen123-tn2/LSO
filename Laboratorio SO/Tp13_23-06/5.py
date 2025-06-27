valor = []
m = int(input("Ingrese número de elementos del arreglo: "))
for i in range(m):
    elemento = int(input("Ingrese Elemento: "))
    valor.append(elemento)

bus = int(input("Ingrese el valor buscado: "))

for i in range(m):
    if valor[i] == bus:
        print("La posición del elemento es", i+1)
        break
