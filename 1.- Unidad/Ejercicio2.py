''' Ejercicio2: Tipos de Datos

2.- Cree un programa con 3 variables 
(texto_1, texto_2, texto_final). 
La primera debe ser la cadena “Este es 
el curso de Python “, la segunda debe ser ” 
de Azul School!” y la última debe ser la 
concatenación de ambas cadenas.

Por último, accede a la última variable 
texto_final para obtener la cadena “Python”, 
utilizando la expresión variable
[posicion_inicial : posicion_final].
'''

texto_1 = "Este es el curso de Python"
texto_2 = " de Azul School"
texto_final = texto_1 + texto_2

print(texto_final + "\n")

print(texto_final[20:26])
