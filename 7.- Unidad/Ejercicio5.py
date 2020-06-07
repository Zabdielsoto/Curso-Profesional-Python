'''Ejercicio 5: Clases
5.- En la clase Guerrero definida en el ejercicio anterior, 
escriba un método atacar que reciba otra instancia 
y disminuya de la vida de la misma en 20.
**Considere el concepto “duck typing”.
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100

	def atacar(self, guerr):
		guerr.vida -= 20


g1 = Guerrero()
g2 = Guerrero()

print("Guerrero 1 sin haber sido atacado")
print(g1.vida, g1.estado_arma)
g2.atacar(g1)
print("\nGuerrero 1 despues de haber sido atacado")
print(g1.vida, g1.estado_arma)
