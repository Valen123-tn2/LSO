m = []
while True: 
    print("Opciones de menu: " \
    "1- Hambuerguesa" \
    "2- Pizza" \
    "3- Ensalada" \
    "4- Salir")
    e = int(input("Ingrese su pedido: "))
    if e == 4: 
        print("su pedido es",m)
        break
    elif e == 1: 
        m.append("Hamburguesa") 
    elif e == 2: 
        m.append("Pizza") 
    elif e == 3: 
        m.append("Ensalada") 

    
