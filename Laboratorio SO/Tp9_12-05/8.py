import random
n = []
par = []
p = 0
for i in range(5): 
    num = random.randint(1,11)
    n.append(num)
print("Los numeros son",n)

for i in range(len(n)): 
    if n[i]%2 == 0: 
        p += 1
        par.append(n[i])
    
print("Hay",p,"Numeros pares y son",par)