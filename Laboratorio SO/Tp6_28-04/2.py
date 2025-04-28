v = float(input("Ingrese la velocidad de su vehiculo: "))
if v <= 60:
    print("Esta dentro del limite de velocidad")
elif v >= 61 and v <= 80:
    print("Esta excediendo levemente el limite de velocidad")
else: 
    print("Esta excediendo gravemente el limite de velocidad")
