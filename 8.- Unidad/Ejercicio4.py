'''Ejercicio 4: Conversion de Tipos
4.- Utilizando collections.defaultdict, cree 
un objeto con el tipo int por defecto. 
Luego, actualice el objeto con los valores de 
la variable ranking_ingredientes del paso anterior. 
Para finalizar, imprima el valor de las claves 
“Pepperoni” y “Pepinillos”; deben devolver 3 y 
0 respectivamente.
'''

from collections import defaultdict
from collections import namedtuple
from collections import Counter

Pizza = namedtuple("Pizza", "tamanyo precio ingredientes")

pedidos = [["Hawaina", "Grande", "Salami"], ["Suprema", "Mediana",
"Carne"], ["Pepperoni", "Chica", "Salami"]]

pizzas = []

for n in pedidos:
	pizzas.append(Pizza(n[0], n[1], n[2]))

ing = []
for n in pizzas:
	ing.append(n.ingredientes)
	print(n)

print(ing)
ranking_ingredientes = Counter(ing)

print("Ingrediente mas comun: ", ranking_ingredientes.most_common(1))

defau = defaultdict(int)
defau.update(ranking_ingredientes)

print(type(defau))
print("Claves: ", defau.keys())
print("Buscar Jamon: ", defau["Jamon"])
print("Claves: ",defau.keys())