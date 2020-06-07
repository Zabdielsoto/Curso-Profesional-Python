'''Ejercicio3: Cadenas
3.- Utilizando métodos de cadenas, identificar 
cuál de las siguientes cadenas posee solo 
caracteres alfabéticos: “Python 3”, “Python3”, 
“Python3.8”
'''

cadena1 = "Python 3"
cadena2 = "Python3"
cadena3 = "Python3.8"

if cadena1.isalnum() is True:
	print(cadena1 + " solo tiene caracteres alfanumericos\n")
else: 
	print(cadena1 + " tiene otros caracteres no alfanumericos\n")

if cadena2.isalnum() is True:
	print(cadena2 + " solo tiene caracteres alfanumericos\n")
else: 
	print(cadena2 + " tiene otros caracteres no alfanumericos\n")

if cadena3.isalnum() is True:
	print(cadena3 + " solo tiene caracteres alfanumericos\n")
else: 
	print(cadena3 + " tiene otros caracteres no alfanumericos\n")