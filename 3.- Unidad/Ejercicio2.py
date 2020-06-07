'''Ejercicio 2: Diccionarios
2.- Recorra la lista en forma directa e 
inversa e imprima sus valores.
'''

pares = [n for n in range(0,11) if n%2 == 0]
print("Lista de Forma Directa")
for n in pares:
	print(n)

print("\nLista de Forma Inversa")
for n in pares[::-1]:
	print(n)