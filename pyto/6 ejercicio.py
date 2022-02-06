"""
entradas
numeor de mujeres--> mujeres
numero de hombres--> hombres
salidas
cantidad de mujeres--> A
cantidad de hombres-->B
"""




mujeres=int(input("numero de mujeres:"))
hombres=int(input("numero de hombres:"))
p=hombres+mujeres
print("total", p)
B=(hombres/p)*100
A=(mujeres/p)*100
print(f"cantidad de mujeres: {int(A)}%" )
print(f"cantidad de hombres: {int(B)}%" ) 