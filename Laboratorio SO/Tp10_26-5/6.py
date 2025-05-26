r =[]
re = 1
tr = 0
md = 0
while re!=0:
    re = int(input("Ingrese el monto donado(ingrese 0 para terminar): "))
    if re == 0: 
        break
    elif re !=0:
        r.append(re)

for i in range(len(r)):
        tr+=r[i]

for i in range(len(r)):
    if r[i] > md:
        md = r[i]

tp = len(r)

print("Aportaron un total de",tp,"personas y se junto en total",tr,"pesos de las donaciones")
print("Siendo la mayor aportacion de",md,"pesos")