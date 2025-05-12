t =[]
tem = 0
men = 0
may = 0
while tem != -100: 
    tem = int(input("Ingrese la temperatura: "))
    if tem != -100:
        t.append(tem)

for i in range(len(t)): 
    if t[i] >= 30: 
        may +=1
    elif t[i] < 0: 
        men += 1

print("Hay",may,"temperaturas mayores o iguales a 30 y",men,"temperaturas menores a 0")