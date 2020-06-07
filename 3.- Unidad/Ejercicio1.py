'''Ejercicio 1: Diccionarios
1.- Cree una lista de números pares del 
0 al 10 utilizando una lista por comprensión.
'''

pares = [n for n in range(0,11) if n%2 == 0]
print("Numeros Pares: ", pares)