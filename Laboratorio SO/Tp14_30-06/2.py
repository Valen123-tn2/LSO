n = int(input("Ingrese la cantidad de elementos: "))
a = []

for i in range(n):
    num = int(input("Ingrese los elementos: "))
    a.append(num)

m = max(a)
sm = 0

for num in a:
    if num != m and num > sm:
        sm = num

else:
    print("El segundo mayor elemento es:", sm)