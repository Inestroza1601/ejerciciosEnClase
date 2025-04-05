import os
os.system('cls' if os.name=='nt' else 'clear')

# Ejercicio 1: Suma de dos números
print("SUMA DE DOS NÚMEROS")
print("----------------------------------------")
# pedimos los datos
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
#calculamos y mostramos los resultados
print(f"La suma de {num1} + {num2} es: {num1+num2}")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 2: Cálculo del área de un triángulo
print("\nCÁLCULO DEL ÁREA DE UN TRIÁNGULO")
print("----------------------------------------")
# pedimos los datos
baseT=int(input("Ingrese el valor de la base: "))
alturaT=int(input("Ingrese el valor de la altura: "))
#calculamos y mostramos los resultados
area=(baseT*alturaT)/2
print("El área del triángulo es:",area)
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 3: Conversión de grados Celsius a Fahrenheit
print("\nCONVERCION DE CELSIUS A FAHRENHEIT")
print("----------------------------------------")
# pedimos los datos
gradosC=float(input("Ingrese los grados Celsius: "))
#calculamos y mostramos los resultados
fahren=(gradosC*9/5)+32
print("Su equivalente en Fahrenheit es:",fahren)
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 4: Calculadora de edad
print("\nCALCULAR LA EDAD DE UNA PERSONA ")
print("----------------------------------------")
# pedimos los datos
anioA=int(input("Igrese el año actual: "))
anioN=int(input("Igrese el año de nacimiento: "))
#calculamos y mostramos los resultados
print(f"Su edad es: {anioA-anioN} años")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 5: Concatenación de nombre completo
print("\nCONCATENACION DE NOMBRE COMPLETO ")
print("----------------------------------------")
#pedimos los datos 
nombre=(input("Ingresa tu nombre: "))
apellido=(input("Igresa tu apellido: "))
#calculamos y mostramos los resultados
print(f"Tu nombre completo es {nombre + " " + apellido}")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 6: Cálculo del perímetro de un rectángulo
print("\nCÁLCULO DEL PERIMETRO DE UN RECTANGULO")
print("----------------------------------------")
# pedimos los datos
anchoR=int(input("Ingrese el valor del ancho: "))
altoR=int(input("Ingrese el valor de la altura: "))
#calculamos y mostramos los resultados
perimetro=(anchoR+altoR)*2
print("El perimetro del rectangulo es:",perimetro)
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 7: Cálculo del promedio de tres notas
print("\nCALCULAR EL PROMEDIO  ")
print("----------------------------------------")
# pedimos los datos
not1=float(input("Igrese la primera nota: "))
not2=float(input("Igrese la segunda nota: "))
not3=float(input("Igrese la tercera nota: "))
#calculamos y mostramos los resultados
prom=(not1 + not2 + not3) / 3
print("El promedio es:",prom,"%")
print("----------------------------------------")
print("FIN DEL PROGRAMA")