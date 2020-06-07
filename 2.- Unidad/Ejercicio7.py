'''Ejercicio 7: Cadenas
7.- Dada una expresión matemática 
“2 * 15 = 30”, cambiar el asterisco 
por una “x” y el signo “=” por la cadena 
“es igual a” utilizando métodos de cadenas. 
**Puede que precises utilizar dos veces el mismo método.
'''

cadena = "2 * 15 = 30"
print("Cadena Original: " + cadena)

cadena1 = cadena.replace('*', 'x')
print("\n Primer Remplazo: " + cadena1)

cadena2 = cadena1.replace('=', 'es igual a')
print("\nSegundo Remplazo: " + cadena2)