p = 0
c = 0
pro = []

while True:
    pr = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if pr == "fin":
        break
    pre = int(input("Ingrese su precio: "))
    can = int(input("Cuanto va a llevar?: "))
    pro.append(pr)
    p += pre
    c += can
   
print("Los productos llevados fueron",pro,"Acumulando un total de",p,"pesos y una cantidad de",c,"items")