"""
entradas
sueldo -> s -> int
venta 1 -> v1 -> int
venta 2 -> v2 -> int
venta 3 -> v3 -> int
salida
su comision es del 10% -> P
el total que ganara es -> p2
"""
#entradas
S=int(input("sueldo"))
v1=int(input("venta 1"))
v2=int(input("venta 2"))
v3=int(input("venta 3"))
#caja negra
P=((v1+v2+v3)/3)*0.10
P2=P+S
#salida
print("el valor de sus comisiones es:",str(P)),
print("el valor total es",str(P2))
