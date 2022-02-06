"""
entrada
lado 1 --> a 
lado 2 --> b
lado 3 --> c
salida
el area es --> A
"""
#entradas

a=int(input("lado 1:"))
b=int(input("lado 2:"))
c=int(input("lado 3:"))
#caja negra
S=((a+b+c)/2)
A=((S*(S-a)*(S-b)*(S-c))**0.5)
#salida
print("su area es", str(A))
