'''Ejercicio 6: Cadenas
6.- Del ejercicio anterior, guardar en 
una variable el valor impreso y volver a 
separar sus valores utilizando métodos de cadenas.
'''

lista = ["2", "4", "6", "8", "10"]

cadena = "-".join(lista)

print("Lista: ", lista)
print("\nCadena Concatenada: " + cadena)

cadena2 = cadena.split(sep = '-')
print("\nCadena Separada: ", cadena2)