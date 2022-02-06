"""
entradas

billetes de 50000 --> n1
billetes de 20000 --> n2
billetes de 10000 --> n3
billetes de 5000 --> n4
billetes de 2000 --> n5
billetes de 1000 --> n6
billetes de 500 --> n7
billetes de 100 --> n8

salidas

cantidad de dinero del banco --> to
"""
#entradas
n1=int(input("cantida de billetes de 50000: "))
n2=int(input("cantida de billetes de 20000: "))
n3=int(input("cantida de billetes de 10000: "))
n4=int(input("cantida de billetes de 5000: "))
n5=int(input("cantida de billetes de 2000: "))
n6=int(input("cantida de billetes de 1000: "))
n7=int(input("cantida de billetes de 500: "))
n8=int(input("cantida de billetes de 100: "))
#caja negra
cant1=n1*50000
cant2=n2*20000
cant3=n3*10000
cant4=n4*5000
cant5=n5*2000
cant6=n6*1000
cant7=n7*500
cant8=n8*100
to=cant1+cant2+cant3+cant4+cant5+cant6+cant7+cant8
#ssalidas
print("su cantidad de dinero es:", str(to))