g = int(input("Ingrese la cantidad de partidos ganados: "))
p = int(input("Ingrese la cantidad de partidos perdidos: "))
e = int(input("Ingrese la cantidad de partidos empatados: "))

g = g*3
p = p*0

t = g+p+e 

print("El puntaje total es:",t)