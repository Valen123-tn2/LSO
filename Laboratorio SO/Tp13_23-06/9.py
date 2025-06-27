animal = []
tamArray = int(input("Ingresar dimensión del array: "))

for x in range(tamArray):
    elemento = input("Ingrese Animal{}: ".format(x+1))
    animal.append(elemento)

nom = input("Ingrese animal buscado: ")
print("El animal tiene como vecino a:")

for x in range(tamArray):
    if animal[x] == nom:
        if x == 0:
            print(animal[x+1])
        elif x == tamArray-1:
            print(animal[x-1])
        else:
            print(animal[x-1])
            print(animal[x+1])
