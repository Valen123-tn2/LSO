p = 300000
g = 1
t = 0
while g !=0:
    g = float(input("Ingrese los gastos(Ponga 0 para terminar): "))
    t = t+g

if t > p: 
    print("El total supera el presupuesto")
elif t <= p:
    print("El presupuesto no fue supearado")