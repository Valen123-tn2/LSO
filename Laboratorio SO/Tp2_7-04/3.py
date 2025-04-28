c = int(input("ingrese el numero de respuestas correctas: "))
i = int(input("ingrese el numero de respuestas incorrectas: "))
b = int(input("ingrese el numero de respuestas  en blanco: "))

c = c*3
i = i * -1
b = b*0

p = c+i+b

print("El puntaje total es:",p)