import os
os.system('cls' if os.name=='nt' else 'clear')
PI=3.1416
#Area y volumen de un cono truncado
#Area y volumen de una esfera
#Area y volumen de un cilindro
#area de una esfera
# A=4*pi*r**2
print("PROGRAMA QUE CALCULA EL AREA DE UNA ESFERA")
print("<------------------------------------------->")
radio=float(input("Ingrese el radio de la esfera: "))
A=4*PI*radio**2
print("el area de la esfera es:",round(A,2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

#Volumen de una esfera ya sea que se use el mismo radio o uno diferente
# V=(4/3)*pi*r**3
print("\nPROGRAMA QUE CALCULA EL VOLUMEN DE UNA ESFERA")
print("<------------------------------------------->")
opcion=input("Es la misma esfera que el ejercicio anterior? (s/n): ")
if opcion=="s" or opcion=="S":
    V=(4/3)*PI*radio**3
else:
    radio=float(input("Ingrese el radio de la esfera: "))
    V=(4/3)*PI*radio**3
print("El volumen de la esfera es:",round(V,2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

#Area de un cono truncado
# A=PI*(r1+r2+g*(r2-r1))
# r1=radio mayor, r2=radio menor, g=generatriz
print("\nPROGRAMA QUE CALCULA EL AREA DE UN CONO TRUNCADO")
print("<------------------------------------------->")
altura=float(input("Ingrese la altura del cono truncado: "))
radioMayor=float(input("Ingrese el radio mayor del cono truncado: "))
radioMenor=float(input("Ingrese el radio menor del cono truncado: "))
#preguntamos si conoce el valor de la generatriz
opcion=input("Conoce el valor de la generatriz? (s/n): ")
#condicionamos si la generatriz es conocida o no
#si la generatriz es conocida se le pide el valor, si no se calcula
if opcion=="s" or opcion=="S":
    generatriz=float(input("Ingrese el valor de la generatriz: "))
else:
    generatriz = ((radioMayor - radioMenor) ** 2 + altura ** 2) ** 0.5
    print("El valor de la generatriz es:",round(generatriz,2))
area = PI * (radioMayor + radioMenor) * generatriz + PI * (radioMayor**2 + radioMenor**2)
print("El area del cono truncado es:",round(area,2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

#Volumen de un cono truncado
# V=(h*pi)/3*(r1**2+r2**2+r1*r2)
# r1=radio mayor, r2=radio menor, h=altura
print("\nPROGRAMA QUE CALCULA EL VOLUMEN DE UN CONO TRUNCADO")
print("<------------------------------------------->")
opcion=input("Es la misma figura que el ejercicio anterior? (s/n): ")
if opcion=="s" or opcion=="S":
    volumen = (PI * altura / 3) * (radioMayor**2 + radioMenor**2 + radioMayor * radioMenor)
else:
    altura=float(input("Ingrese la altura del cono truncado: "))
    radioMayor=float(input("Ingrese el radio mayor del cono truncado: "))
    radioMenor=float(input("Ingrese el radio menor del cono truncado: "))
    volumen = (PI * altura / 3) * (radioMayor**2 + radioMenor**2 + radioMayor * radioMenor)
print("El volumen del cono truncado es:",round(volumen,2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

#Area de un cilindro
# A=2*pi*r**2+2*pi*r*h
# r=radio, h=altura
print("\nPROGRAMA QUE CALCULA EL AREA DE UN CILINDRO")
print("<------------------------------------------->")
radio=float(input("Ingrese el radio del cilindro: "))
altura=float(input("Ingrese la altura del cilindro: "))
area=(2*PI*radio**2)+(2*PI*radio*altura)
print("El area del cilindro es:",round(area,2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

#Volumen de un cilindro
# V=pi*r**2*h
# r=radio, h=altura
print("\nPROGRAMA QUE CALCULA EL VOLUMEN DE UN CILINDRO")
print("<------------------------------------------->")
opcion=input("Es la misma figura que el ejercicio anterior? (s/n): ")
if opcion=="s" or opcion=="S":
    volumen=PI*radio**2*altura
else:
    radio=float(input("Ingrese el radio del cilindro: "))
    altura=float(input("Ingrese la altura del cilindro: "))
    volumen=PI*radio**2*altura
print("El volumen del cilindro es:",round(volumen,2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")