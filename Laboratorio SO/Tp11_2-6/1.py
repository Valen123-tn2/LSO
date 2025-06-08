p = []
n =[]
c = []
for i in range(20): 
    num = int(input("Ingrese un numero:"))
    if num%2 == 0:
        if num == 0:
            c.append(num)
        else: 
            p.append(num)
    elif num%2 !=0:
        n.append(num)
po = len(p)
ne = len(n)
ce = len(c)

print("hay",po,"Numeros positivos,",ne,"Numeros negativos y",ce,"Ceros.")