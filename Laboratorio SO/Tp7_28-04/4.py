ing = float(input("Ingrese sus ingresos: "))
g = []
c = []
while True:
    cat = input("Ingrese una categoría de gasto(fin si quiere dejar de ingresar): ")
    if cat == "fin":
        break
    mon = float(input("Ingrese el monto para la categoria: "))
    c.append(cat)
    g.append(mon)
    

gt = 0 
i = 0
while i < len(g):
    gt = gt + g[i]
    i += 1

st = ing-gt

i = 0
while i < len(g):
    p = 0 
    p = (g[i]/ing)*100
    print(c[i], ":", g[i],"(",p,"%)")
    i += 1

print("Gasto total:",gt)
print("Ingreso total:",ing)
print("Saldo restante:",st)