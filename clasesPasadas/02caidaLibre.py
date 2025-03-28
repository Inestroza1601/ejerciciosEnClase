#formulas:
    #Vf = Vi + g*t
    #     donde:
    #         Vf = velocidad final
    #         Vi = velocidad inicial
    #         t = tiempo
    #         g = gravedad

    # Y = Yi + Vi*t + 1/2*g*t^2
    #     donde:
    #         Y = altura
    #         Yi = altura inicial
    #         Vi = velocidad inicial 
    #         t = tiempo
    #         g = gravedad

    # Vf^2 = Vi^2 + 2*g*(Y - Yi)
    #     donde:
    #         Vf = velocidad final
    #         Vi = velocidad inicial
    #         g = gravedad
    #         Y = altura final
    #         Yi = altura inicial
from math import sqrt
print("RESUELVE ECUACIONES DE CAIDA LIBRE")
# Mostramos las opciones
print("\n1. Vf=Vo+gt | 2. Y=Yo+Vot+(1/2)gt^2 | 3. Vf^2=Vo^2+2g(Y)")

# Condicionales para elegir la ecuación a resolver
opcion = int(input("\nDigite el número de la ecuación a resolver: "))
#definimos la constante
G = 9.8

#evaluamos que opcion fue seleccionada y calculamos
if opcion == 1:
    print("Vf=Vo+gt")
    print("------------------------------")
    Vi = float(input("Digite la velocidad inicial (m/s): "))
    t = float(input("Digite el tiempo (s): "))
    Vf = Vi + (G * t)  # Realizamos el cálculo
    print(f"La velocidad final es: {Vf:.2f} m/s^2") # Mostramos los resultados formateado para que muestre solo dos decimales
elif opcion == 2:
    print("Y=Yo+Vot+1/2gt^2")
    print("------------------------------")
    Yi = float(input("Digite la altura inicial: "))
    if Yi<0:
        print("La altura inicial no puede ser 0")
        exit()
    Vi = float(input("Digite la velocidad inicial: "))
    if Vi<0:
        print("La altura velocidad no puede ser 0")
        exit()
    t = float(input("Digite el tiempo: "))
    if t<0:
        print("El tiempo no puede ser 0")
        exit()
    Y = Yi + Vi * t + (1/2) * G * t**2 # Realizamos el cálculo
    print(f"La altura final es: {Y:.2f} m")  # Mostramos los resultados formateado para que muestre solo dos decimales
elif opcion == 3:
    print("Vf^2=Vo^2+2g(Y)")
    print("------------------------------")
    Vi = float(input("Digite la velocidad inicial: "))
    if Vi<0:
        print("La altura velocidad no puede ser 0")
        exit()
    Yi = float(input("Digite la altura inicial: "))
    if Yi<0:
        print("La altura inicial no puede ser 0")
        exit()
    Y = float(input("Digite la altura final: "))
    Vf = sqrt(Vi**2+2*G*(Y)) # Realizamos el cálculo
    print(f"La velocidad final es: {Vf:.2f} m/s^2")  # Mostramos los resultados formateado para que muestre solo dos decimales
else:
    print("La opción seleccionada no es válida")
print("------------------------------")
print("PROGRAMA TERMINADO CON EXCITO")
input()