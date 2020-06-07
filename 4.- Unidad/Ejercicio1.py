'''Ejercicio 1: Funciones
1.- Escriba una función que, recibiendo el 
valor de una matriz de 2 dimensiones, 
imprima la misma con el caracter “X”. Ej, 4×3:
'''
#Definimos una funcion, con un parametro que es una lista
def funcion(l):
	''' Parametro l, de tipo lista, con dos sublistas de misma 
		longuitud con numeros enteros dentro de ellas

		Funcion devuelve serie de impresiones tomando los 
		elementos que tengan la misma posicion en las sublistas
		y colocando el caracter x entre ellos
	'''

	#El iterable a recorrer se obtiene primero obteniendo la 
	#longuitud de la segunda sublista de la lista en el parametro
	#l, despues con range se obtiene un iterable, como solo
	#se espcifica un parametro en range, por defecto se toma
	#como que el iterable va desde 0 hasta llegar al numero 
	#indicado en el parametro, de 0 a 3 en este caso 
	for n in range(len(l[1])):
		print(l[0][n], "X", l[1][n])

matriz = [[1, 2, 3],[1, 2, 3]]

funcion(matriz)