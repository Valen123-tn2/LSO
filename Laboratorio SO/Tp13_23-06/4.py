V = 100*[0]
i = 0
n = int(input("Ingrese tamaño del vector: "))
opc = -1

while opc != 0:
    print("1) Añadir elemento")
    print("2) Eliminar elemento")
    print("3) Listar vector")
    print("4) Contar apariciones")
    print("5) Media y máximo")
    print("0) Terminar")
    opc = int(input("Ingrese Opción: "))

    if opc == 1:
        if i < n:
            V[i] = int(input("Ingrese Entero: "))
            i += 1

    elif opc == 2:
        num = int(input("Ingrese el número que desea eliminar: "))
        a = -1
        for j in range(i):
            if V[j] == num:
                a = j
                break
        if 0 <= a < i:
            for j in range(a, i-1):
                V[j] = V[j+1]
            V[i-1] = 0
            i -= 1

    elif opc == 3:
        for j in range(i):
            print(V[j])

    elif opc == 4:
        num = int(input("Ingrese número para contar: "))
        c = V[:i].count(num)
        print("El número de apariciones es:", c)

    elif opc == 5:
        if i > 0:
            maximo = max(V[:i])
            media = sum(V[:i]) / i
            print("El máximo es:", maximo, " y la media es:", media)

    elif opc == 0:
        print("FIN DE PROGRAMA")
