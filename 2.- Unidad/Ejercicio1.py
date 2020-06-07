'''Ejercicio 1: Cadenas
1.- Dada la cadena “El veloz murciélago
hindú comía feliz cardillo y kiwi”, 
imprimir su variante justificada a la 
derecha rellenando con ‘>’, a la izquierda 
rellenando con ‘<‘ y centrada en 60 
caracteres con asteriscos utilizando métodos de cadenas.
'''
cadena = "El veloz murcielago hindu comia feliz cardillo y kiwi"

print("Cadena Original \n" + cadena)

cadena1 = cadena.rjust(60,'>')
print("\nJustificada a la Derecha \n" + cadena1)

cadena2 = cadena.ljust(60, '<')
print("\nJustificada a la izquiera \n" + cadena2)

cadena3 = cadena.center(60, '*')
print("\n Centrada \n" + cadena3)