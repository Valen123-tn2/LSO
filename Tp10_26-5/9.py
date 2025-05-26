md = 20000
while md!=0:
    mg= float(input("Ingrese el monto gastado: "))
    md-=mg
    if md == 0:
        print("Su monto diario fue alcanzado, no podra seguir comprando")
        break
    