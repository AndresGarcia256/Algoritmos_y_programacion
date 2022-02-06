"""
entrada
horas --> S
sueldo por hora --> S2
salida
tu sueldo es --> R2
"""
#entradas
S=int(input("horas:"))
S2=int(input("sueldo por hora:"))
#caja negra
R=S2*0.80
R2=R*S
#salida
print("sueldo final", R2)