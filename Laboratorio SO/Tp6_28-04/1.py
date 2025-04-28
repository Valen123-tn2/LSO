e = int(input("Ingrese su edad: "))

if e < 18: 
    print("Es menor de edad")
elif e > 18 and e < 64: 
    print("Es adulto")
else: 
    print("Es un adulto mayor")