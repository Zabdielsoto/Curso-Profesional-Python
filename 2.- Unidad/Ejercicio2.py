'''Ejercicio 2: Cadenas
Dada la cadena "Nuevo curso de Python 3",
usar los metodos de cadena e imprimir
a) Su variante en mayusculas
b) Su variante en minusculas
c) Su variante intercambiando mayusulas y 
minusculas
d) Convertir el primer caracter de cada
palabra a mayuscula
'''

cadena = "Nuevo curso de Python 3"
print("Cadena Original \n" + cadena)

cadena1 = cadena.upper()
print("\n Cadena en Mayusculas \n" + cadena1)

cadena2 = cadena.lower()
print("\n Cadena en Minusculas \n" + cadena2)

cadena3= cadena.swapcase()
print("\n Intercambiando mayusculas y minusculas \n" + cadena3)

cadena4 = cadena.title()
print("\nPrimer caracter de cada palabra en mayuscula \n"+ cadena4)