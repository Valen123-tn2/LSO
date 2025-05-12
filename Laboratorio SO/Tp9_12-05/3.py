p = []
pre = 1 
while pre != 0: 
    pre = int(input("Ingrese el precio: "))
    if pre != 0:
        p.append(pre)

t = sum(p)

if t > 10000: 
    t = t-t*0.10

print("El total es de",t)