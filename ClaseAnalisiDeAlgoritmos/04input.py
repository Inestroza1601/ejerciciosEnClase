# input en python
import os
os.system('cls' if os.name=='nt' else 'clear')

cadena=input("Ingrese un texto: ")
a=int(input("igrese el primer numero: "))
b=int(input("igrese el segundo numero: ")) 
#operaciones aritmeticas
# + suma
suma=a+b
print(f"\nLa suma de {a} + {b} es: {suma}")
print("---------------------------------")
# - resta
resta=a-b
print(f"La resta de {a} - {b} es: {resta}")
print("---------------------------------")
# * multiplicacion
multi=a*b
print(f"La multiplicacion de {a} * {b} es: {multi}")
print("---------------------------------")
# / divicion
div=a/b
print(f"La divicion de {a} / {b} es: {div}")
print("---------------------------------")
# ** potencia
pot=a**2
pot2=b**2
print(f"La potencia de {a} es: {pot}")
print(f"La potencia de {b} es: {pot2}")
print("---------------------------------")