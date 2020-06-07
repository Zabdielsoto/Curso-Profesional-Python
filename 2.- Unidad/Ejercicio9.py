'''Ejercicio 9: Cadenas
9.- Codifica la cadena 
“El veloz murciélago hindú comía feliz cardillo y kiwi” 
a una secuencia de bytes con utf-16, 
guarda el valor en una variable y 
luego vuelve a decodificarla para imprimir la cadena.
'''

cadena = "El veloz murciélago hindú comía feliz cardillo y kiwi"
print("Cadena original: " + cadena)

cadena1 = cadena.encode(encoding = "utf-16", errors = "strict")
print("\nCadena Codificada: ", cadena1)

cadena2 = cadena1.decode(encoding = "utf-16", errors = "strict")
print("\nCadena Decodificada: " + cadena2)