te = 0
d = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
for i in range(7):
    print("Dia:", d[i])
    ed = float(input("Ingrese minutos de ejercicio que hizo:" ))
    te +=ed

p = te/7

if p > 30: 
    print("Hace un promedio de",int(p),"minutos de ejercicio por dia")
elif p <= 30: 
    print("Toma un promedio de",int(p),"minutos de ejercicio por dia, recomendaria aumentar los minutos de ejercicio")