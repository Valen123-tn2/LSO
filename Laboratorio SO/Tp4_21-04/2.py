s = float(input("Ingrese su sueldo: "))
if s<1000: 
    s = s + s*0.15
    print("su sueldo ahora es de: $",s)
else: 
    print("su sueldo es de:",s)