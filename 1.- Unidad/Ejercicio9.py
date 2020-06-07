'''Ejercicio Propuesto 9: Tipos de Datos

2.- Utilizando la sentencia while, 
escriba un programa que imprima los 
múltiplos de 3 hasta que la sumatoria de 
todos los valores imprimidos sea mayor a 50.
'''
multiplos = 0
suma = 0

while(suma <= 50):
	print(multiplos)
	suma += multiplos
	multiplos += 3
else: 
	print("Ciclo Terminado")
