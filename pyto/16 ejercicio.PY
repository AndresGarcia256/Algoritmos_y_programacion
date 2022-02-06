"""

entradas

cantidad de galones --> galon

salidas

precio --> preciofin

"""
#entradas

galon=int(input("cantidad de galones:"))
#caja negra
preciolitro=50000*3.785
preciofin=galon*preciolitro
#salida
print("su precio es:", preciofin)
