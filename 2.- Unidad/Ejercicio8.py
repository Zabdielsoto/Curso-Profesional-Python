'''Ejercicio 8: Cadenas
8.- Dada la expresión “{1} * {2} = {0}”.format(15, #, #), 
reemplaza los numerales para que la cadena 
sea una expresión válida.
'''

cadena1 = "{1} * {2} = {0}"
print("Cadena Original: " + cadena1)

cadena2 = cadena1.format(15, 3, 5)
print("\nCadena formateada: " + cadena2)