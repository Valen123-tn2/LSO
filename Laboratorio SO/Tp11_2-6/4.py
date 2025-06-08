n =[]
num = 0
fr = []
no = 0
while no !=-1:
    no = int(input("Ingrese las notas (-1 para salir): "))
    if no == -1:
        break
    elif no >= 1 and no <= 10:
        n.append(no)
        num += no
    else:
        fr.append(no)

p = num/len(n)
tfr = len(fr)

print("El promedio de las notas es de",p,"con",tfr,"notas fuera de rango")