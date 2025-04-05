import os
os.system('cls' if os.name=='nt' else 'clear')

# Notas de 4 parciales en un arreglo

notas=[0,0,0,0]
print("Ingrese notas")
notas[0]=int(input("Igrese nota 1: "))
notas[1]=int(input("Igrese nota 2: "))
notas[2]=int(input("Igrese nota 3: "))
notas[3]=int(input("Igrese nota 4: "))
sumarNotas=notas[0]+notas[1]+notas[2]+notas[3]
promedio=sumarNotas/4
print("<------------------------>")
print("EL promedio es:",promedio)

if promedio>=70:
    print("\nAprobó")
else:
    print("\nReprobó!")

## calificaciones
# 0-49 NO TIENE DERECHO A RECUPERACION
# 50-69 NO SATISFACTORIO
# 70-80 BUENO
# 81-90 MUY BUENO
# 91-100 EXCELENTE

if promedio>=0 and promedio<50:
    print("NO TIENE DERECHO A RECUPERACIÓN")
elif promedio>=50 and promedio<70:
    print("NO SATISFACTORIO")
elif promedio>=70 and promedio<81:
    print("BUENO")
elif promedio>=81 and promedio<91:
    print("MUY BUENO")
elif promedio>=91 and promedio<=100:
    print("EXCELENTE")
else:
    print("VALOR FUERA DE LOS PARAMETROS")
#<--------------------------------------------------->
#LO MISMO PERO SIN ANIDACION
if promedio>=0 and promedio<50:
    print("NO TIENE DERECHO A RECUPERACIÓN")

if promedio>=50 and promedio<70:
    print("NO SATISFACTORIO")

if promedio>=70 and promedio<81:
    print("BUENO")

if promedio>=81 and promedio<91:
    print("MUY BUENO")

if promedio>=91 and promedio<=100:
    print("EXCELENTE")