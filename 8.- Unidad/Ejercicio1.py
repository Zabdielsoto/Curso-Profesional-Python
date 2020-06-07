'''Ejercicio 1: Conversion de Tipos
1.- Importe namedtuple y utilizando la misma, 
cree una clase Pizza con los atributos tamanyo, 
precio e ingredientes. 
Luego, cree una lista vacía pizzas
'''

from collections import namedtuple

Pizza = namedtuple("Pizza", "tamanyo, precio, ingredientes")

pizzas = []