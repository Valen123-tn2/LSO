a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el ultimo numero: "))

if a > b and a > c: 
    if b > c:
        print(a,b,c)
    elif c > b:
        print(a,c,b)
if b > a and b > c: 
    if a > c:
        print(b,a,c)
    elif c > a:
        print(b,c,a)
if c > b and c > a: 
    if b > a:
        print(c,b,a)
    elif a > b:
        print(c,a,b)