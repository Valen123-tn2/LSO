p_a = int(input("Ingrese el precio del aparato: "))
m_a = input("Ingrese la marca del aparato: ")
p = 0
p_t = 0
if p_a <= 2000 and m_a == "nosy": 
    p = p_a*0.90
    p_t= p*0.95
elif p_a <= 2000 and m_a != "nosy": 
    p_t= p_a*0.90
elif p_a < 2000 and m_a == "nosy": 
    p = p_a*0.95
    p_t = p + p*0.20
elif p_a < 2000 and m_a != "nosy": 
    p = p_a*1.20 

print("El precio a pagar sera",p_t)



