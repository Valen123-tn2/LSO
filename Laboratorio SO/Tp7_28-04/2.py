print("1- libras a kilogramos")
print("2- kilometros a millas")
print("3- Grados celsius a fahrenheit")
um = input("Ingrese la unidad de medida que quiere: ")
c = float(input("Ingrese la cantidad: "))
if um == 1: 
    k = c*0.453592
elif um == 2: 
    m = c*0.621371
elif um == 3: 
    f = (c*9/5)+32
else:
    print("error")