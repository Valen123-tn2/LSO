ta = 0
d = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
for i in range(7):
    print("Dia:", d[i])
    va = float(input("Ingrese los vasos de agua que tomo:" ))
    ta +=va

p = ta/7

if p > 8: 
    print("Toma un promedio de",p,"vasos de agua por dia")
elif p < 8: 
    print("Toma un promedio de",p,"Vasos de agua por dia, recomendaria aumentar el consumo de agua")