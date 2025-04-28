a = int(input("Ingrese el año: "))
if a%400 == 0 or a%4 == 0 and a%100 !=0: 
    print("El año es bisiesto")
else: 
    print("El año no es bisiesto")