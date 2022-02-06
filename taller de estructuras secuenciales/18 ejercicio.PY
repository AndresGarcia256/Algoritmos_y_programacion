"""

entradas

cantidad de bolivares --> bolivares
tasa de interes --> tasa
tiempo de la inversion --> tiempo 

salidas

valor del interes --> interes
porcentaje por año --> p%

"""
#entradas
bolivares=int(input("cantidad de bolivares:"))
tasa=int(input("cual es su tasa de interes:"))
tiempo=int(input("tiempo de inversion:"))
#caja negra
interes=(bolivares*tasa*tiempo)/100
p=(interes/tiempo)
#salida
print("valor del interes", interes)
print("porcentaje por año", p, "%")