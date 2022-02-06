"""
entradas

chelines austriacos a pesetas --> chas
conversionde drasgmas griegos a francoss francés --> N
ingrese cantidad de dolares a pesetas --> dolares
ingrese cantidad de liras a pesetas --> liras

salidas

cantidad de chelines austriacos --> chaspe
cantidad de francos frances --> francofrances
de dolares acantidad de pesetas --> DOlares1
de liras cantida de pesetas --> liras1
"""

chas=int(input("chelines austriacos a pesetas:"))
chaspe=9568.71*chas
print("su cantidad de chelines austriacos es:", chaspe)

N=int(input("conversionde drasgmas griegos a francoss francés:"))
drgrpe=88607
fran=20110
francofrances=((drgrpe*N)/fran)/100
print("cantidad de francos frances: ", francofrances)

Dolares=int(input("ingrese cantidad de dolares:"))
DOlares1=122499*Dolares
print("su cantidad de pesetas es:", DOlares1)

liras=int(input("ingrese cantidad de liras:"))
liras1=liras*92.89
print("su cantida de pesetas es:", liras1)

