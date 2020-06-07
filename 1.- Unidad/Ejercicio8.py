'''Ejercicio Propuesto 8: Tipos de Datos

1.- Dada una lista de valores numéricos, 
determine e imprima si la sumatoria de 
todos los valores excede a un valor máximo 
establecido en una variable.
'''

valores = [1, 2, 3, 4, 5]
maximo = 20
suma = 0

for valor in valores:
	suma += valor

if suma > maximo:
	print("Se supero el maximo")
else: 
	print("No se supero el maximo")

print(suma)