'''Ejercicio 5: Conversion de tipos
5.- Obtenga e imprima en pantalla el precio mínimo 
y máximo de cada tamaño de pizza existente en la 
lista “pizzas”. Considere utilizar defaultdict.
'''

from collections import defaultdict
from collections import namedtuple
from collections import Counter

Pizza = namedtuple("Pizza", "tamanyo precio ingredientes")

pedidos = [["Grande", 20, "Salami"], ["Chica", 15,
"Carne"], ["Mediana", 10, "Salami"]]

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
#print(ranking_ingredientes)
'''
print(type(defau))
print("Claves: ", defau.keys())
print("Buscar Jamon: ", defau["Jamon"])
print("Claves: ",defau.keys())
'''
p = defaultdict(int)

for n in pizzas:
	p.update({n.tamanyo : [n.precio]})

p.update({"Grande" : [20, 21, 22]})
p.update({"Mediana" : [15, 16, 17]})
p.update({"Chica" : [10, 11, 12]})

#print(p)
p.update()
for n in p:
	print("Maximo en el tamaño ", n, max(p[n]))
	print("Minimo en el tamaño ", n, min(p[n]), "\n")
