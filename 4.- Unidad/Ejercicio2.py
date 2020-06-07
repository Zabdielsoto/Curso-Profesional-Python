'''Ejercicio 2: Funciones
2.- Tomando 3.14 como valor de PI, escriba 
una función que reciba el valor del radio 
de un círculo y retorne el valor de su área:
'''

PI = 3.14
radio = 2

def area(r):
	a = PI * (r ** 2)
	return a

resultado = area(radio)
print(resultado)