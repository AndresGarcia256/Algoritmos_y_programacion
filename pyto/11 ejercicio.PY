"""
entradas

nombre --> nombre
cantidad de niños --> demonios
cuanto pagan la hora --> ht
horas trabajadas --> h
horas extras --> he
250000 --> actaca
173000 --> precio_por_demonio
180000 --> prima

salidas
el sueldo --> st
valor de los impuestos --> deducciones
valor de las asignaciones --> asig
el sueldo total --> sueldototal

"""
#entradas
nombre=(input("como es tu nombre:"))
demonios=int(input("¿cuantos hijos tienes?:"))
ht=int(input("valor de las horas trabajas:"))
h=int(input("horas tranajadas:"))
he=int(input("horas extras:"))
actaca=250000
precio_por_demonio=173000
prima=180000
#caja negra
h2=h*ht
he2=h2*1.25
st=h2+he2
deducciones=st*0.14
asig=(actaca+prima)+(173000*demonios)
#salida
print("su sueldo es:", st)
print("el valor de los impuestos es:", deducciones)
print("el valor de sus asignaciones", asig)
#caja negra
sueldotolal=(st+asig-deducciones)
#salida
print("su sueldo total es:", sueldotolal)