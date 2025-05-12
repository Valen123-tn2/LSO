import random
l = int(input("Ingrese la longitud que quiere: "))
print("1- Letras")
print("2- Numeros")
print("3- Simbolos")
print("4- Letras y numeros")
print("5- Letras y simbolos")
print("6- simbolos y numeros")
print("7- Todos")

c = int(input("Ingrese lo que quiere usar: "))
ca = ""
let = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sim = "!@#$%^&*()-_=+[]{};:,.<>?/"

if c == 1: 
    ca = ca + let
elif c == 2: 
    ca = ca + num
elif c == 3: 
    ca = ca + sim
elif c == 4: 
    ca = ca + let + num
elif c == 5: 
    ca = ca + let + sim
elif c == 6: 
    ca = ca + sim + num 
elif c == 7: 
    ca = ca + let + num + sim 
co = ""
i = 0
while i < l: 
    gr = random.randint(0, len(ca) - 1)
    co = co + ca[gr]
    i = i+1

print("La contraseña es: ", co)