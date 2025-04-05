import os
os.system('cls' if os.name=='nt' else 'clear')

#condicion si o if
x=int(input("igrese un numero: "))
if x>=0:
    print("El numero es positivo")
else:
    print("El numero es negativo")