"""
resultados de las diferentes calificaciones
inserte nota 1 con valor de 55%"-->N1
inserte nota 2 con valor de 55%"-->N2
inserte nota 3 con valor de 55%"-->N3
inserte nota total 4 con valor de 30%-->nota4
inserte nota total 5 con valor de 15%-->nota5
salidas
promedio de las notas segun sus porcentajes-->T 
"""
#entradas
N1=int(input("inserte nota 1 con valor de 55%"))
N2=int(input("inserte nota 2 con valor de 55%"))
N3=int(input("inserte nota 3 con valor de 55%"))
nota4=int(input("inserte nota total 4 con valor de 30%"))
nota5=int(input("inserte nota total 5 con valor de 15%"))
#caja negra
M=((N1+N2+N3)/3)
M1=M*0.55
M2=nota4*0.30
M3=nota5*0.15
T=M1+M2+M3
#salida
print("su nota es", T)

