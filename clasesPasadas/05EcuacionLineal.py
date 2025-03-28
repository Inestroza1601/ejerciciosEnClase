#pycharm
#ecuacion lineal

import os
os.system('cls' if os.name=='nt' else 'clear')

print("ECUACION LINEAL")
print("aX+b=0   X=-b/a")

a=float(input("igrese a: "))
b=float(input("ingrese b: "))


X=-b/a

print(a,"X +",b,"=0")
print("X=",X)