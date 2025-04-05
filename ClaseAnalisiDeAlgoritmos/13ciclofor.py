import os
os.system('cls' if os.name=='nt' else 'clear')

#programa que pida tres productos
precio=[100,200,300]
#calcular el tatal a pagar
cantidad=0
totalPagar=0

for i in range(len(precio)):
    cantidad=int(input(f"Igrese la cantidad del producto que vale {precio[i]} Lps.: "))
    totalPagar+=cantidad*precio[i]
print(f"El total a pagar es {totalPagar} Lps.")