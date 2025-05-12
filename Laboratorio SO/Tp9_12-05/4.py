import random

n = random.randint(1,11)
i = 0
print(n)

while i < 3:
    u = float(input("Ingrese un numero del 1 al 10: "))
    if u == n: 
        print("¡Acertaste!")
        break
    elif u != n: 
        print("¡Incorrecto!")
        i +=1

if i == 3 and u != n: 
    print("Perdiste")

