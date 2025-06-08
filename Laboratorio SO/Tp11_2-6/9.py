tv = 0
vm = 0

while True:
    p = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if p == "fin":
        break

    c = int(input("Ingrese la cantidad que quiere llevar: "))
    pu = float(input("Ingrese el precio unitario del producto: "))

    t = c * pu
    tv += t

    if t > 1000:
        vm += 1

print("El total vendido fue de",tv)
print("Con",vm,"ventas superando los $1000")
   