t = [["hola","pendiente"]]
while True: 
    print("1- Ver tareas")
    print("2- Agregar tarea")
    print("3- Eliminar tarea")
    print("4- Actualizar estado de tarea")
    print("5- Salir")
    a = int(input("Ingrese la accion a hacer: "))
    if a == 1: 
        if not t: 
            print("No hay tareas")
        else: 
            for i in range(len(t)): 
                print("sus tareas son:",t)
    elif a == 2: 
        n = input("Ingrese el nombre de la tarea: ")
        t.append([n, "pendiente"])
        print("Listo, ya esta agregada")
    elif a == 3: 
        if not t: 
            print("No hay tareas para eliminar")
        else:
            for i in range(len(t)):
                 print(i+1,t[i]) 
            n = int(input("Ingrese el numero de tarea a eliminar: "))
            t.pop(n-1)
            print("Listo eliminada")
    elif a == 4:
        if not t: 
            print("No hay tareas para eliminar") 
        else:
            for i in range(len(t)): 
                print(i+1,t[i][0],t[i][1]) 
            n = int(input("Que tarea quieres actualizar: "))
            print("1- Pendiente")
            print("2- En Progreso")
            print("3- Completada")
            ec = int(input("Seleccione el estado que queire aplicar: "))
            if ec == 1:
                t[n-1][1] = "Pendiente"
                print("Listo, Hecho")
            elif ec == 2:
                t[n-1][1] = "En Progreso" 
                print("Listo, Hecho")
            elif ec == 3: 
                t[n-1][1] = "Completada"
                print("Listo, Hecho")
    elif a == 5:
        break

 
            


   