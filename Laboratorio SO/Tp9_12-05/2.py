e = []
n = 0
a = 0
ad = 0
ed = 1
while ed != 0: 
    ed = int(input("Ingrese la edad: "))
    if ed != 0:
        e.append(ed)

for i in range(len(e)): 
    if e[i] < 13: 
        n += 1
    elif e[i] >= 13 and e[i] <= 17: 
        a += 1
    elif e[i] >= 18:
        ad += 1

print("Hay: ",n,"Niños",a,"Adolecentes",ad,"Adultos")
