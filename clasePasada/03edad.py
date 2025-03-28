#programa para calcular la edad dependiendo del año de nacimiento

#delcaracion de variables
anioActual=2025
#Pedimos al usuario su año de nacimiento
anioNacimiento=int(input("Ingrese su año de nacimiento: "))
nombre=input("Ingrese su nombre: ")
#Realizamos el calculo
edad=anioActual-anioNacimiento
print("Hola",nombre,"Su edad es",edad,"Años")