import os
os.system('cls' if os.name=='nt' else 'clear')

from datetime import datetime
from datetime import timedelta

añoActual = datetime.now().year

def Edad(fN, aA):
    return aA-fN

añoN=int(input("Ingrese su año de nacimiento: "))
print(f"Su edad es: {Edad(añoN,añoActual)}")