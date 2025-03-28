# pide al usuario una cadena de texto
# {	"Print to console": {
# 		"scope": "python",
# 		"prefix": "cadenaDeTexto",
# 		"body": [
# 			"=input(\"Ingrese un texto: \")"
# 		],
# 		"description": "Declara una variable de texto"
# 	}
# }
# <---------------------------------------------------------------------------->

# inserta el bloque elegir de lenguaje latino
# {	"Print to console": {
# 		//"scope": "javascript,typescript","
# 		"prefix": "elegir",
# 		"body": [
# 			"imprimirf(\"Digite la operacion a realizar: \")",
# 			"opcion=leer()",
# 			"elegir(cadena.mayusculas(opcion))",
# 			"  caso 1:",
# 			"",
# 			"  caso 2:",
# 			"",
# 			"  defecto:",
#     		"    imprimir(\"Opcion no valida\")",
# 			"fin",
# 			"$2"
# 		],
# 		"description": "Evalúa una opción en múltiples casos posibles y selecciona uno de varios bloques de códigos para ser ejecutados."
# 	}
# }
# <---------------------------------------------------------------------------->

# inserta un hola mundo en python
# {	"Print to console": {
# 		"scope": "javascript,typescript,python",
# 		"prefix": "hola",
# 		"body": [
# 			"print(\"hola mundo!\")",
# 			"$2"
# 		],
# 		"description": "Imprime un hola mundo en pantalla"
# 	}
# }
# <---------------------------------------------------------------------------->

# limpia la terminal de comandos en python
# {	"Print to console": {
# 		"scope": "python",
# 		"prefix": "limpiar",
# 		"body": [
# 			"import os",
# 			"os.system('cls' if os.name=='nt' else 'clear')",
# 			"$1"
# 		],
# 		"description": "Limpia la pantalla de la consola"
# 	}
# }
# <---------------------------------------------------------------------------->

# agrega una pausa al final del programa para evitar que se cierre
# {	"Print to console": {
# 	//"scope": "javascript,typescript",
# 	"prefix": "pausa",
# 	"body": [
#  		"pausa=leer()",
#  		"$2"
#  	],
# 	"description":"Genera una pausa en el programa"
# 	 }
# }
# <---------------------------------------------------------------------------->

# inserta un prinf en python
# {	"Print to console": {
# 		"scope": "javascript,typescript,python",
# 		"prefix": "printf",
# 		"body": [
# 			"print(f\"Hola, mi nombre es {$1} y tengo {$2} años.\")",
# 		],
# 		"description": "print F"
# 	}
# }
# <---------------------------------------------------------------------------->

# pide al usuario un decimal
# {	"Print to console": {
# 		"scope": "javascript,typescript,python",
# 		"prefix": "variableDecimal",
# 		"body": [
# 			"=float(input(\"igrese el numero: \"))",
# 			"$1"
# 		],
# 		"description": "Declara una variable decimal"
# 	}
# }
# <---------------------------------------------------------------------------->

# pide al usuario un numero entero
# {	"Print to console": {
# 		"scope": "javascript,typescript,python",
# 		"prefix": "variableEntero",
# 		"body": [
# 			"=int(input(\"igrese el primer numero: \"))",
# 			"$2"
# 		],
# 		"description": "Delcalra una variable entera"
# 	}
# }