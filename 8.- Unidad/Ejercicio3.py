'''Ejercicio 3: Conversion de Tipos
3.- Utilizando collections.Counter, 
cree un objeto ranking_ingredientes que 
contenga todos los ingredientes de las 
instancias en la lista “pizzas” 
(incluyendo repetidos). Luego imprima el 
ingrediente más utilizado con la cantidad 
de pedidos que incluyeron el mismo.
** La impresión debe devolver [(‘Queso’, 6)]
'''

import collections

Pizza = collections.namedtuple("Pizza", "tamanyo precio ingredientes")

pedidos = [["Hawaina", "Grande", "Salami"], ["Suprema", "Mediana",
"Carne"], ["Pepperoni", "Chica", "Salami"]]

pizzas = []
#print(pedidos)
#pizzas.append(Pizza(pedidos[0][0], pedidos[0][1], pedidos[0][2]))
for n in pedidos:
	pizzas.append(Pizza(n[0], n[1], n[2]))

ing = []
for n in pizzas:
	ing.append(n.ingredientes)
	print(n)

print(ing)
ranking_ingredientes = collections.Counter(ing)

print("Ingrediente mas comun: ", ranking_ingredientes.most_common(1))
print(ranking_ingredientes)