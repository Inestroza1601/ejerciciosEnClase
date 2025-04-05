#definir los tipos de variables
import os
os.system('cls' if os.name=='nt' else 'clear')

#variables de tipo entero
a = 104
A = 105 #python discrimina entre mayusculas y minusculas
variable = 106
VARIABLE = 107
Variable = 108
print(a)

#variables de tipo flotante, decimales
b = 10.4
B = 10.5
opcion = 10.6
Opcion = 10.7
OPCION = 10.8
print(b)

#variables tipo cadena
c = "Hola Mundo"
C = "Hola Mundo"
nombre="Lucas"
apellido="Tañeda"
print(c)

#varibles tipo booleano
d = True
D = False
print(d)

#variables de tipo lista
e = [10,42,3,88,5]
E = ["Hola", "Mundo", "Python"]
print(e)
print(e[3])

#variables tipo tupla
f = (1,2,3,4,5)
F = ("Hola", "Mundo", "Python")
print(f)
print(f[3])

#variables de tipo diccionario
g = {"Nombre":"Juan", "Edad":30, "Telefono":"1234567890"}
print(g)
print("Nombre:",g["Nombre"])
print("Edad:",g["Edad"])
print("Telefono:",g["Telefono"])

print(f"El resultado de sunar {a} + {b} es: {a+b}")
print(f"Su nombre completo es: {nombre + " " + apellido}")