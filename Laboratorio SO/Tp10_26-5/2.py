cl = 1
tc = 0
pt = []
cm = 0
while cl != 0: 
    cl = float(input("Ingrese la cantidad de litros cargados(ingrese 0 para finalizar): "))
    if cl == 0:
        break
    elif cl < 5: 
        cm = cm+1
        tc = tc+cl
        pt.append(cl)
    elif cl > 5: 
        tc+=cl
        pt.append(cl)

pc = tc/len(pt)

if cm != 0: 
    print("¡Alerta! hubo",cm,"Cargas minimas")
    print("El total cargado fue de:",tc,"Litros con un promedio de",pc,"Litros por carga")
else:
    print("El total cargado fue de:",tc,"Litros con un promedio de",pc,"Litros por carga")