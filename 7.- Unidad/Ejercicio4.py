'''Ejercicio 4: Clases
4.- Cree una clase Guerrero que posea los 
atributos “vida” con valor inicial en 100 
y “estado_arma” con valor inicial en 100.
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100

g1 = Guerrero()

print(g1.vida, g1.estado_arma)