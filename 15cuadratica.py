import os
os.system('cls' if os.name=='nt' else 'clear')

#cacular formula cuadratica
def cuadratica(a,b,c):
    ##1
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    ##2
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    #imprimir las soluciones
    print(f"x1={x1}")
    print(f"x2={x2}")

##programa
print("Ecuacion Cuadratica aX^2+bX+c=0")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
#invocamos funcion cuadratica
cuadratica(a,b,c)