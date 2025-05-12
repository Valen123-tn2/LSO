n = 1234
i = 0
while i < 3:
    c = float(input("Ingrese un numero la contraseña: "))
    if c == n: 
        print("Correcto, Entrando al Sistema")
        break
    elif c != n: 
        print("Contraseña Incorrecta")
        i +=1

if i == 3 and c != n: 
    print("Incorrecto, Bloqueando el Acceso al Sistema")
