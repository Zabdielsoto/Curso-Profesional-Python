'''Ejercicio 3: Diccionarios
3.- Data la lista 
[“radar”, “palabra”, “reconocer”, “frase”, “aves”, “perdiz”], 
recorra sus elementos con un ciclo for 
e imprima un mensaje si la misma es un palíndromo.
'''

lista = ["radar", "palabra", "reconocer", "frase", "aves", 
		"perdiz"]

for n in lista:
	if n == n[::-1]:
		print(n + " es un palindromo")