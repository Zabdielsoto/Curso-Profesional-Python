'''Ejercicio 3: Funciones
3.- Cree una función que, recibiendo una 
lista de números, retorne una lista con 2 
elementos, la primera debe ser una lista de 
pares y el segundo una lista de impares.
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def separar(l):
	pares = []
	impares = []
	for n in l:
		if n%2 == 0:
			pares.append(n)
		elif n%2 == 1:
			impares.append(n)

	return [pares,impares]

resultado = separar(lista)
print("Pares: ", resultado[0])
print("\nImpares: ", resultado[1])