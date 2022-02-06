"""

entradas

precio al contado --> P
precio por cuotas --> T

salidas

porcentaje de recargo --> porcentaje%

"""
#entradas
P=int(input("precio al contado:"))
T=int(input("precio por cuotas:"))
#caja negra.
precio=(T*12)
recargo=(precio-P)
porcentaje=(recargo*100/P)
#salida
print("el porcentaje de recargo es:", str(porcentaje), "%")

