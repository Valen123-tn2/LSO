a = []
for i in range(5): 
    al = float(input("Ingrese la nota del alumno: "))
    a.append(al)

p = sum(a)/len(a)
    
if p >= 7:
    print("El promedio es mayor a 7","Es de:",p)
else: 
    print("El promedio no supera los 7","Es de:",p)