#operaciones aritmeticas
# + suma
import os
os.system('cls' if os.name=='nt' else 'clear')
a=10
b=5
suma=a+b
print("La suma de a y b es:",suma)
print(a,"+",b,"=",suma)
print(f"la suma de {a} + {b} es: {suma}")
print("------------------------------------")
# - resta
resta=a-b
print("La resta de a y b es:",resta)
print(a,"-",b,"=",resta)
print(f"la resta de {a} - {b} es: {resta}")
print("------------------------------------")
# * multiplicacion
multiplicacion=a*b
print("La multiplicacion de a y b es:",multiplicacion)
print(a,"*",b,"=",multiplicacion)
print(f"la multiplicacion de {a} * {b} es: {multiplicacion}")
print("------------------------------------")
# / division
division=a/b
print("La division de a y b es:",division)
print(a,"/",b,"=",division)
print(f"la division de {a} / {b} es: {division}")

#**potencia
cuadrado=a**2
print(f"la potenvia de {a} es: {cuadrado}")

#raiz
raizCuadra= b**0.5
print(f"La raiz de {b} es {raizCuadra}")