n1 = 0
n2 = 1

while True:
    ns = n1 + n2
    if ns >10000:
        break
    print(ns)
    n1 = n2
    n2 = ns