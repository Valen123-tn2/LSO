""" 1 """
"""c = int(input("Ingrese la calificacion del alumno: "))
if c > 10: 
    print("El alumno esta aprobado")
else: 
    print("El alumno esta desaprobado")"""

""" 2 """
"""s = float(input("Ingrese su sueldo: "))
if s<1000: 
    s = s + s*0.15
    print("su sueldo ahora es de: $",s)
else: 
    print("su sueldo es de:",s)"""

""" 3 """
"""a = int(input("Ingrese el año: "))
if a%400 == 0 or a%4 == 0 and a%100 !=0: 
    print("El año es bisiesto")
else: 
    print("El año no es bisiesto")"""

""" 4 """
"""o = int(input("Ingrese la operacion a realizar(1,2,3): "))
n = int(input("Ingrese el numero a usar: "))

if o == 1: 
    n = 100*n
    print("El resultado es:",n)
elif o == 2: 
    n = 100**n
    print("El resultado es:",n)
elif o == 3: 
    n = 100/n 
    print("El resultado es:",n)
else: 
    print("operacion inexistente")"""

""" 5 """
"""n = int(input("Ingrese el numero a leer: "))
if n%2 == 0: 
    print("El numero es par")
else: 
    print("El numero es impar")"""

""" 6 """
"""a = int(input("Ingrese el primer numero: "))
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
        print(c,a,b)"""