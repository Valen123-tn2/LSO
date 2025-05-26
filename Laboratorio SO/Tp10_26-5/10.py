com = 0
ck = 0.07

while True:
    print("1.Cargar")
    print("2.Consumo")
    print("3.Detener")
    i = int(input("Ingrese que quiere hacer: "))
    
    if i == 3: 
        break

    elif i == 1: 
        ca = float(input("Ingrese la cantidad de litros a cargar: "))
        com+=ca
    
    elif i == 2: 
        con = float(input("Ingrese el consumo: "))
        com-=con
        if com <= 0: 
            print("No hay compustible suficiente")
    
if com >= 50*ck:
    print("Hay combustible pra 50km mas")
else: 
    print("No hay suficiente combustible par 50km mas")
            
    
    

