'''Ejercicio 2: Conversion de tipos
2.- Dada la lista “pedidos”, agruéguela al código, 
recorra la misma, cree instancias de la clase Pizza 
y agregue las mismas a la lista “pizzas”.
'''

import collections

Pizza = collections.namedtuple("Pizza", "tamanyo precio ingredientes")

pedidos = [["Hawaina", "Grande", "Pinia"], ["Suprema", "Mediana",
"Carne"], ["Pepperoni", "Chica", "Salami"]]

pizzas = []
#print(pedidos)
#pizzas.append(Pizza(pedidos[0][0], pedidos[0][1], pedidos[0][2]))
for n in pedidos:
	pizzas.append(Pizza(n[0], n[1], n[2]))

for n in pizzas:
	print(n)