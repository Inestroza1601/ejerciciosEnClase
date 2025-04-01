import os
os.system('cls' if os.name=='nt' else 'clear')

PI = 3.1416

# Funciones para cálculos geométricos
def areaEsfera(radio):
    a = 4 * PI * radio ** 2
    return a

def volumenEsfera(radio):
    v = (4/3) * PI * radio ** 3
    return v

def areaConoTruncado(radioMayor, radioMenor, altura, generatriz=None):
    if generatriz is None:
        generatriz = ((radioMayor - radioMenor) ** 2 + altura ** 2) ** 0.5
    a = PI * (radioMayor + radioMenor) * generatriz + PI * (radioMayor**2 + radioMenor**2)
    return a

def volumenConoTruncado(radioMayor, radioMenor, altura):
    v = (PI * altura / 3) * (radioMayor**2 + radioMenor**2 + radioMayor * radioMenor)
    return v

def areaCilindro(radio, altura):
    a = (2 * PI * radio ** 2) + (2 * PI * radio * altura)
    return a

def volumenCilindro(radio, altura):
    v = PI * radio ** 2 * altura
    return v

print("PROGRAMA QUE CALCULA EL AREA Y VOLUMEN DE DIFERENTES FIGURAS")
print("-------------------------------------------------------------")

# Área de una esfera
print("\nPROGRAMA QUE CALCULA EL AREA DE UNA ESFERA")
print("<------------------------------------------->")
radio = float(input("Ingrese el radio de la esfera: "))
print("El área de la esfera es:", round(areaEsfera(radio), 2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

# Volumen de una esfera
print("\nPROGRAMA QUE CALCULA EL VOLUMEN DE UNA ESFERA")
print("<------------------------------------------->")
opcion = input("¿Es la misma esfera que el ejercicio anterior? (s/n): ")
if opcion.lower() != "s":
    radio = float(input("Ingrese el radio de la esfera: "))
print("El volumen de la esfera es:", round(volumenEsfera(radio), 2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

# Área de un cono truncado
print("\nPROGRAMA QUE CALCULA EL AREA DE UN CONO TRUNCADO")
print("<------------------------------------------->")
altura = float(input("Ingrese la altura del cono truncado: "))
radioMayor = float(input("Ingrese el radio mayor del cono truncado: "))
radioMenor = float(input("Ingrese el radio menor del cono truncado: "))
opcion = input("¿Conoce el valor de la generatriz? (s/n): ")
if opcion.lower() == "s":
    generatriz = float(input("Ingrese el valor de la generatriz: "))
    print("El área del cono truncado es:", round(areaConoTruncado(radioMayor, radioMenor, altura, generatriz), 2))
else:
    print("El área del cono truncado es:", round(areaConoTruncado(radioMayor, radioMenor, altura), 2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

# Volumen de un cono truncado
print("\nPROGRAMA QUE CALCULA EL VOLUMEN DE UN CONO TRUNCADO")
print("<------------------------------------------->")
opcion = input("¿Es la misma figura que el ejercicio anterior? (s/n): ")
if opcion.lower() != "s":
    altura = float(input("Ingrese la altura del cono truncado: "))
    radioMayor = float(input("Ingrese el radio mayor del cono truncado: "))
    radioMenor = float(input("Ingrese el radio menor del cono truncado: "))
print("El volumen del cono truncado es:", round(volumenConoTruncado(radioMayor, radioMenor, altura), 2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

# Área de un cilindro
print("\nPROGRAMA QUE CALCULA EL AREA DE UN CILINDRO")
print("<------------------------------------------->")
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))
print("El área del cilindro es:", round(areaCilindro(radio, altura), 2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")

# Volumen de un cilindro
print("\nPROGRAMA QUE CALCULA EL VOLUMEN DE UN CILINDRO")
print("<------------------------------------------->")
opcion = input("¿Es la misma figura que el ejercicio anterior? (s/n): ")
if opcion.lower() != "s":
    radio = float(input("Ingrese el radio del cilindro: "))
    altura = float(input("Ingrese la altura del cilindro: "))
print("El volumen del cilindro es:", round(volumenCilindro(radio, altura), 2))
print("<------------------------------------------->")
print("FIN DEL PROGRAMA")