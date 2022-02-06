"""

entradas

precio naranjas--> X
valor de la docena --> Y
precio a la venta --> K

salidas

porcentaje de ganancias --> porcentaje%

"""
#entradas
X=int(input("precio naranjas"))
Y=int(input("valor docena"))
K=int(input("precio de venta"))
#caja negra
X1=(X/12)
Y2=(Y*X1)
K2=(K-Y2)
porcentaje=(K2*100)/Y2

#salida
print("su porcentaje es", porcentaje ,"%")