s = 20
sm = s*0.10
cs = 1

while cs !=0 or s !=0: 
    cs = int(input("Ingrese la candidad de articulos vendidos(ingrese 0 para finalizar): "))
    s = s-cs
    if cs == 0:
        break
    if s <= sm: 
        print("¡Queda menos del 10% del stock original!")
    if s == 0:
        print("Ya no hay stock")
        break


if s != 0: 
    print("Quedan",s,"articulos")