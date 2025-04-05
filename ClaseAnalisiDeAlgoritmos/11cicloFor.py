import os
os.system('cls' if os.name=='nt' else 'clear')
#ciclo for en python
for i in range(1,11):
    print(f"5 x {i} = {5*i}")

tabla=int(input("Ingrese la tabla que desea visualizar: "))
for i in range(1,11):
    print(f"{tabla} x {i} = {tabla*i}")