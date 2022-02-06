"""

entradas

cantidad de presupuesto --> presupuesto

salidas

presupuesto para ginecologia 40% --> presupuesto1
presupuesto para traumatologia 30% --> presupuesto2
presupuesto para pediatria 30% --> presupuesto3

"""
#entradas
presupuesto=int(input("cantidad de presupuesto:"))
#caja negra
presupuesto1=presupuesto*0.40
presupuesto2=presupuesto*0.30
presupuesto3=presupuesto*0.30
#salida
print("presupuesto para ginecologia:", presupuesto1)
print("presupuesto para traumatologia:", presupuesto2)
print("presupuesto para pediatria:", presupuesto2)