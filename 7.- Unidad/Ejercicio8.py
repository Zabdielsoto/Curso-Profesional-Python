'''Ejercicio 8: POO
8.- A la clase Guerrero, agregue una propiedad 
“is_alive” (@property) que indique si el objeto 
está vivo (posee una vida mayor a 0).
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100
		#self._is_alive = True


	@property
	def is_alive(self):
		if self.vida > 0:
			return True
		else:
			return False

	def atacar(self, guerr):
		guerr.vida -= 20
		if self.estado_arma >= 2:
			self.estado_arma -= 2
		else:
			print("El arma no tiene suficiente poder")


g1 = Guerrero()
g2 = Guerrero()

g2.estado_arma = 1
print("Guerrero 1 sin haber sido atacado")
print(g1.vida, g1.estado_arma)
print("\nGuerrero 2 antes de atacar")
print(g2.vida, g2.estado_arma)
g2.atacar(g1)
print("\nGuerrero 1 despues de haber sido atacado")
print(g1.vida, g1.estado_arma)
g2.vida = 0
print("\nGuerrero 2 despues de atacar")
print(g2.vida, g2.estado_arma, g2.is_alive)
g2.vida = 100
print(g2.vida, g2.estado_arma, g2.is_alive)