"""

entradas

digite lectura actual --> lect1 
digite lectura lectura --> lect2
valor de kilovatio --> valor

salidas

su total --> total

"""
#entradas
lect1=int(input("digite lectura actual"))
lect2=int(input("digite lectura lectura"))
valor=int(input("valor de kilovatio"))
#caja negra
consumo=(lect2-lect1)
total=consumo*valor
#salida
print("su total es:", str(total))
