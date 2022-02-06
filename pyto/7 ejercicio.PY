"""
entradas
metros-->A
pies-->ft
pulgadas--> pulgada
salidas
metros en pies --> R
metrso en pulgadas --> R1
"""
#entradas
A=int(input("metros:"))
ft=3.28084
pulgada=39.27
#caja negra
R=A*ft
R1=A*pulgada
#salida
print("sus metros en pies son:", R)
print("sus metros en pulgasdas son:", R1)