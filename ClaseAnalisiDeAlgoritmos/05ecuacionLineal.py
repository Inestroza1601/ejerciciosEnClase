#programa que resuelve la ecuacion lineal
import os
os.system('cls' if os.name=='nt' else 'clear')

print("ECUACION LINEAL aX+b=0")
a=int(input("Ingrese el valor de a:"))
b=int(input("Ingrese el valor de b:"))

X=-b/a
print(f"el valor de X es:{X}")