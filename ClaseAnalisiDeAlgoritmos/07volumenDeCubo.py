#calcular el area y el volumen de un cubo
import os
os.system('cls' if os.name=='nt' else 'clear')

print("CALCULAR EL AREA Y VOLUMEN DE UN CUBO")
print("-------------------------------------")
lado=int(input("Ingrese el valor del lado: "))
#realizamos la operacion
area=6*(lado**2)
volumen=lado**3
print(f"El area del cubo es: {area}")
print(f"El volumen del cubo es: {volumen}")
print("-------------------------------------")
print("FIN DEL PROGRAMA")