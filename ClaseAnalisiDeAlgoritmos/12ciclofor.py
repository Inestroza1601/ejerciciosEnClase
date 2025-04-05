#notas con ciclo for y un arreglo
import os
os.system('cls' if os.name=='nt' else 'clear')

notas=[0,0,0,0]
sumNotas=0
print("Ingrese notas")
for i in range(len(notas)):
    notas[i]=int(input(f"Igrese nota paracial[{i+1}]: "))
    sumNotas+=notas[i]
# print(notas)
# print(sumNotas)
print(f"El promedio es: {sumNotas/len(notas)}%")