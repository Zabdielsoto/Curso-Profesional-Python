'''Ejercicio Propuesto 4: Tipos de Datos

1.- Cree una lista de 5 elementos con 
valores del 1 al 5. Luego, agregue un 
elemento obteniendo el valor del tercer 
elemento de la lista (posición 2). 
Para finalizar, encuentre la posición del 
valor 3 y elimine la misma.
'''

lista = [1, 2, 3, 4, 5]

print(lista, "\n\n")

lista.append(lista[2])

print(lista, "\n\n")

print("Posicion del numero 3: ", lista.index(3))

lista.pop(lista.index(3))

print(lista)



