te = []
ind = int(input("Ingrese la cantidad de temperaturas a agregar: "))
mm =[]
mi = 0
tt = 0
for i in range(ind):
    tem = float(input("Ingrese temperatura: "))
    te.append(tem)
    tt += te[i]

m = tt/ind

for i in range(len(te)):
    if te[i] >= m:
        mi += 1
        mm.append(te[i])

print("La cantidad de temperaturas mayores a la media fueron",mi,"siendo las temperaturas de",mm)