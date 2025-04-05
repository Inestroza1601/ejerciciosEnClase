import os
os.system('cls' if os.name=='nt' else 'clear')

# tipos de datos
# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("PRGORMA HOLA MUNDO")
print("----------------------------------------")
print("¡Hola Mundo!")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
print("\nPRGORMA HOLA MUNDO CON VARIABLE")
print("----------------------------------------")
saludo="¡Hola Mundo!"
print(saludo)
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla 
# la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
print("\nPROGRAMA SALUDO PERSONALIZADO")
print("----------------------------------------")
nombre=input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
# ((3+2)/(2*5))2
print("\nOPERACION ARITMETICA")
print("----------------------------------------")
operacion = ((3+2)/(2*5)) ** 2
print("El resultado de la operación es:",operacion)
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.
print("\nPROGRAMA QUE CALCULA EL PAGO DE UN TRABAJADOR")
print("----------------------------------------")
horas=float(input("Ingrese las horas trabajadas: "))
pagoHora=float(input("Ingrese el pago por hora: "))
pago=horas*pagoHora
print(f"El pago del trabajador por {horas} horas trabajadas a {pagoHora} lps. por hora es: {pago}")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 6
# Escribir un programa que lea un entero positivo, n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
# n. La suma de los primeros enteros positivos puede ser calculada de la siguiente forma: suma=n*(n+1)/2
print("\nPROGRAMA QUE CALCULA LA SUMA DE LOS PRIMEROS NÚMEROS ENTEROS")
print("----------------------------------------")
n=int(input("Ingrese un número entero positivo: "))
total=n*(n+1)/2
print(f"La suma de los del 1 al {n} números enteros es: {total}")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule
# el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la
# frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa
# corporal calculado redondeado con dos decimales.
print("\nPROGRAMA QUE CALCULA EL INDICE DE MASA CORPORAL")
print("----------------------------------------")
peso=float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su estatura en m: "))
imc=peso/(altura)**2
imc=round(imc,2)
print("Su indice de masa corporal(imc) es:",imc)
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
# la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los
# números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
print("\nPROGRAMA QUE MUESTRE EL COCIENTE Y EL RESIDUO DE UNA DIVICION")
print("----------------------------------------")
n=int(input("Inglese el valor de n: "))
m=int(input("Ingrese el valor de m: "))
print(f"El cociente de {n} / {m} es: {n//m}")
print(f"El residuo de {n} / {m} es: {n%m}")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
# el número de años, y muestre por pantalla el capital obtenido en la inversión.
print("\nPROGRAMA QUE CALCULA EL CAPITAL OBTENIDO EN UNA INVERSION")
print("----------------------------------------")
cantidad=float(input("Ingrese la cantidad a invertir: "))
interes=float(input("Ingrese el interes anual: "))/100
años=int(input("Ingrese el número de años: "))
capital=cantidad*(1+interes*años)
print(f"El capital obtenido en la inversión es: {capital}")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele
# hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así
# que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a
# demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el
# número de payasos y muñecas vendidos en el último pedido y calcule el peso total del
# paquete que será enviado.
print("\nPROGRAMA QUE CALCULA EL PESO TOTAL DE UN PAQUETE")
print("----------------------------------------")
PAYASO=112
MUNECA=75
payasos=int(input("Ingrese el número de payasos vendidos: "))
muñecas=int(input("Ingrese el número de muñecas vendidas: "))
pesoTotal=((PAYASO*payasos)+(MUNECA*muñecas))
print(f"El peso total del paquete que será enviado es: {pesoTotal} gramos")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 11
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés
# al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se
# te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience
# leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el
# usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros
# tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
print("\nPROGRAMA QUE CALCULA EL SALDO DE UNA CUENTA DE AHORROS")
print("----------------------------------------")
INTERES = 4 / 100
Deposito = float(input("Ingrese la cantidad depositada: "))
balance = Deposito
for i in range(1, 4):
    balance = balance * (1 + INTERES)
    print(f"Las ganancias para el año {i} son:", round(balance, 2))
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 12
# Una panadería vende barras de pan a 3.49 Lps. cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
print("\nPROGRAMA DE PANADERIA")
print("----------------------------------------")
VALORU=3.49
DESCUENTO = 60/100
numeroDeBarras=int(input("Ingrese la cantidad de barras que no son del dia: "))
total=numeroDeBarras*VALORU
print(f"El precio habitual es:",VALORU,"Lps")
descuento=total*DESCUENTO
print("Descuento por no ser fresco:",DESCUENTO*100,"%")
print("El total a pagar es:",round(total-descuento,2),"Lps.")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicios de Cadenas
# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número
# entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
# como el número introducido.
print("\nPROGRAMA QUE IMPRIME N CANTIDAD DE VECES EL NOMBRE")
print("----------------------------------------")
nombre=input("Ingrese su nombre: ")
num=int(input("Ingrese un numero: "))
for i in range(1,num+1):
    print(f"{i}-. {nombre}")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y
# después muestre por pantalla el nombre completo del usuario tres veces, una con todas
# las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera
# letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su
# nombre combinando mayúsculas y minúsculas como quiera.
print("\nPROGRAMA QUE IMPRIME EL NOMBRE EN MAYUSCULAS, MINUSCULAS E INTERLADO")
print("----------------------------------------")
nombre=input("Ingrese su nombre completo: ")
print(nombre.lower)
print(nombre.upper)
print(nombre.title)
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de
# que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
# donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
# que tienen el nombre.
print("\nPROGRAMA QUE CUENTE LAS LETRAS DEL NOMBRE")
print("----------------------------------------")
nombre=input("Ingres su nombre: ").upper()
n=len(nombre)
print(f"{nombre} tiene {n} letras.")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
# donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por
# ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de
# teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
print("\nPROGRAMA QUE PREGUNTA UN NUMERO DE TELEFONO")
print("----------------------------------------")
num=input("INGRESE EL NUMERO DE TELEFONO: ")
print('El número de teléfono es ', num[4:-3])
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
print("\nPROGRAMA QUE INVIERTE UNA FRASE ")
print("----------------------------------------")
palabra=input("Igrese una frase: ")
print(palabra[::-1])
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una
# vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en
# mayúscula.
print("\nPROGRAMA QUE REMPLAZA UNA VOCAL")
print("----------------------------------------")
palabra = input("Introduce una frase: ")
letra = input("Introduce una vocal en minúscula:  ")
print(palabra.replace(letra, letra.upper()))
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y
# muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de
# la arroba @) pero con dominio ceu.es.
print("\nPROGRAMA QUE CAMBIA EL DOMINIO")
print("----------------------------------------")
correo=input("Igrnse su correo electronico: ")
print(correo[:correo.find('@')] + '@ceu.es')
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con
# dos decimales y muestre por pantalla el número de euros y el número de céntimos del
# precio introducido.
print("\nPROGRAMA QUE MUESTRA EL PRECIO")
print("----------------------------------------")
valor = input("Introduce el precio del producto con dos decimales: ")
print(valor[:valor.find('.')], 'Lps. y', valor[valor.find('.')+1:], 'centavos.')
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior
# para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
print("\nPROGRAMA QUE MUESTRA LA EDAD DE UNA PERSONA")
print("----------------------------------------")
nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")
partes = nacimiento.split('/')
if len(partes) == 3:
    dia, mes, año = partes
    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {año}")
else:
    print("Formato incorrecto. Asegúrese de usar dd/mm/aaaa")
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 10
# Escribir un programa que pregunte por consola por los productos de una cesta de la
# compra, separados por comas, y muestre por pantalla cada uno de los productos en
# una línea distinta.
print("\nPROGRAMA PRODUCTOS DE UNA CESTA")
print("----------------------------------------")
productos = input("Ingrese los productos de la cesta: ")
lista_productos = [producto.strip() for producto in productos.split(',')]
for producto in lista_productos:
    print(producto)
print("----------------------------------------")
print("FIN DEL PROGRAMA")

# Ejercicio 11
# Escribir un programa que pregunte el nombre el un producto, su precio y un número
# de unidades y muestre por pantalla una cadena con el nombre del producto seguido
# de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
# tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
print("\nPROGRAMA QUE PREGUNTA EL NOMBRE, PRECIO Y UNIDADES DE UN PRODUCTO")
print("------------------------------------------------------")
nombre = input('Introduce el nombre del producto: ')
valor = float(input('Introduce el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
total = unidades * valor
print(f"{nombre}: {unidades:3d} unidades x {valor:9.2f}Lps. = {total:11.2f}Lps.")
print("------------------------------------------------------")
print("FIN DEL PROGRAMA")