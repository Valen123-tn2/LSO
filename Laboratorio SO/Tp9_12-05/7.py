n = []
neg = []
pos = []
for i in range(10): 
    num = float(input("Ingrese un numero: "))
    n.append(num)

for i in range(len(n)): 
    if n[i] < 0: 
        neg.append(n[i])
    elif n[i] > 0:
        pos.append(n[i])

pn = sum(neg)/len(neg)
pp = sum(pos)/len(pos)

print("Hay un total de",len(pos),"Numeros positivos, y su promedio es de",pp)
print("Hay un total de",len(neg),"Numeros negativos, y su promedio es de",pn)