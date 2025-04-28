a = int(input("Ingrese el Año: "))
m = int(input("Ingrese el Mes: "))
d = int(input("Ingrese el Dia: "))

if d > 0 and d > 30: 
    print("Mañana es:",d+1,m,a)
else: 
    if m > 0 and m < 12: 
        print("Mañana es:",1,m+1,a)
    else: 
        print("Mañana es:",1,1,a+1)