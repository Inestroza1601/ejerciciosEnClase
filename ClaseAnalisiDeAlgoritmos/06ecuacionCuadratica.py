#ecuacion cuadratica
import os
os.system('cls' if os.name=='nt' else 'clear')

print("ECUACION CUADRATICA ax^2+bx+c=0")
print("---------------------------------")

a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))

#realizamos la operacion

X1=(-b+(b**2-4*a*c)**0.5)/(2*a)
X2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print("---------------------------------")
print("el valor de X1 es:",X1)
print("el valor de X2 es:",X2)