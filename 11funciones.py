import os
os.system('cls' if os.name=='nt' else 'clear')

#funciones en python
#funcion

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def divicion(a,b):
    return a/b

def potencia(a,b):
    return a**b
# operaciones aritmeticas
print("operaciones aritmeticas")
x=int(input("a: "))
y=int(input("b: "))

# s=suma(2,2)
#s=suma(x,y)
print(s)
print(f"{x} + {y}{suma(x,y)}")
print(f"{x} - {y}{resta(x,y)}")
print(f"{x} * {y}{multiplicacion(x,y)}")
print(f"{x} / {y}{divicion(x,y)}")
print(f"{x} ^ {y}{potencia(x,y)}")