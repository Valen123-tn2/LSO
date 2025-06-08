ac = []
d = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
for i in range(7):
    print("Dia:", d[i])
    ed = float(input("Ingrese minutos de ejercicio que hizo:" ))
    ac.append(ed)

p = sum(ac)/7
ma = max(ac)
mra = min(ac)
dm = ""
dme = ""
for i in range(7):
    if ac[i] == ma and dm == "":
        dm = d[i]
    if ac[i] == mra and dme == "":
        dme = d[i]
print("Hace un promedio de",int(p),"minutos de actividad fisica semanal")
print("Siendo el",dm,"el dia con mayor actividad con",ma,"minutos")
print("Y",dme,"Siendo el dia con menor actividad, con",mra,"minutos")