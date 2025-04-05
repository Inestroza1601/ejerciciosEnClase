#programa que muestre si un numero es par o impar
import os
os.system('cls' if os.name=='nt' else 'clear')
contadorPar=0
contadorImpar=0

for j in range(150):
    if(j%2==0):
        contadorPar+=1
    else:
        contadorImpar+=1

print(f"Pares = {contadorPar}")
print(f"Pares = {contadorImpar}")

##buscar los multiplos de 7

multiplo7=0
for k in range(500):
    if(k%7==0):
        multiplo7+=1
print(f"De 0 a 500 hay {multiplo7} multiplos de 7")