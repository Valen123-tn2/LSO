n = int(input("Ingrese un numero: "))
r = []
for i in range(1,13):
    r.append(n*i)

for i in range(len(r)):
    print(n,"x",i+1,"=",r[i])