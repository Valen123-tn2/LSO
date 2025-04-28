o = int(input("Ingrese la operacion a realizar(1,2,3): "))
n = int(input("Ingrese el numero a usar: "))

if o == 1: 
    n = 100*n
    print("El resultado es:",n)
elif o == 2: 
    n = 100**n
    print("El resultado es:",n)
elif o == 3: 
    n = 100/n 
    print("El resultado es:",n)
else: 
    print("operacion inexistente")