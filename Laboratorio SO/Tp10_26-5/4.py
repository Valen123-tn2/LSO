a = 0
d = 0
for i in range(10):
    n = float(input("Ingrese la nota del alumno: "))
    if n >= 6:
        a +=1
    elif n < 6: 
        d +=1

print("Aprobaron",a,"Alumnos y desaprobaron",d,"Alumnos")