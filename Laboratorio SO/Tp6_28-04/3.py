m = []
while True: 
    print("Opciones de menu: ")
    print("1- Hambuerguesa")
    print("2- Pizza")
    print("3- Ensalada") 
    print("4- Salir")
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
    else: 
        print("Error")

    
