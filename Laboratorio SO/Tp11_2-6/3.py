n = int(input("Ingrese un numero: "))
primo = ""
for i in range(2,n):
    if n % i == 0:
        primo = "no"

if primo == "no": 
    print("El numero no es primo")
else:
    print("El numero es primo")
