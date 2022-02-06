"""

entradas

valor nota matematicas examen --> matesexam
valor nota matematicas tarea 1 --> mates1
valor nota matematicas tarea 2 --> mates2
valor nota matematicas tarea 3 --> mates3
valor nota fisica exam --> fisiexam
valor nota fisica tarea 1  --> fisica1
valor nota fisica tarea 2 --> fisica2
valor nota quimica exam --> quimiexam
valor nota quimica tarea 1 --> quimica1
valor nota quimica tarea 2 --> quimica2
valor nota quimica tarea 3 --> quimica3

salidas

nota matematicas --> notafmat
nota fisica  --> notasfisi
nota matematica  --> notas qui
promedio de sus notas  --> total

"""
#entradas

matesexam=int(input("valor nota matematicas exam:"))
mates1=int(input("valor nota matematicas tarea 1:"))
mates2=int(input("valor nota matematicas tarea 2:"))
mates3=int(input("valor nota matematicas tare 3:"))
fisiexam=int(input("valor nota fisica exam:"))
fisica1=int(input("valor nota fisica tarea 1:"))
fisica2=int(input("valor nota fisica tarea 2:"))
quimiexam=int(input("valor nota quimica exam:"))
quimica1=int(input("valor nota quimica tarea 1:"))
quimica2=int(input("valor nota quimica tarea 2:"))
quimica3=int(input("valor nota quimica tarea 3:"))

#caja negra-salidas

print("empezemos por matematicas bro, yo se que pasas")
tareasmat=((mates1+mates2+mates3)/3)*0.10
notafmat=tareasmat+(matesexam*0.90)
print("mates nota final:", notafmat)
print("vamos con fisica")
tareasfisi=((fisica1+fisica2)/2)*0.20
notasfisi=tareasfisi+(fisiexam*0.80)
print("tu nota final de fisica es:", notasfisi) 
print("vamos con quimica")
tareasquimi=((quimica1+quimica2+quimica3)/3)*0.15
notasqui=tareasquimi+(quimiexam*0.85)
print("notas quimica", notasqui)
total=(notasfisi+notafmat+notasqui)/3
print("promedio general", total )
A=(input("¿como te fue?"))
