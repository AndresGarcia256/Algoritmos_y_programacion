"""

entradas

precio de venta --> prven
precio final --> prfin

salidas

porcentaje --> m2
 
"""
#entradas
prven=int(input("precion de venta"))
prfin=int(input("precion final"))
#caja negra
m=(prven-prfin)
m2=(m*100)/prven
#salida
print("el porcentaje es", m2)

