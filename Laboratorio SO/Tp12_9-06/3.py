e = []
ec = []
ind = int(input("Ingrese el numero de elementos a agregar: "))

if ind >= 1 and ind <= 200:
    for i in range(1,ind+1): 
        ele = int(input("Ingrese el elemento: "))
        e.append(ele)

for i in range(len(e)):
    if e[i] not in ec:
        ec.append(e[i])

ec.sort()

print("Lista completa y ordenada:",ec)
