import os
os.system('cls' if os.name=='nt' else 'clear')

#programa que muestre un arreglo de 5 valores y que los sumen
e = [10,42,3,88,5]
suma=(e[0]+e[1]+e[2]+e[3]+e[4])
print(f"la suma de {e[0]} + {e[1]} + {e[2]} + {e[3]} + {e[4]} es:",suma)