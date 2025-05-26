tt = 0
tm = 0
d = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
for i in range(7):
    print("Dia:", d[i])
    td = float(input("Ingrese la temperatura del dia: " ))
    tt +=td
    if td >= 30: 
        tm +=1

m = tt/7

print("La media de temperatura fue de",int(m),"con",tm,"dia superando los 30 grados")