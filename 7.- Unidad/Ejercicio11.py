'''Ejercicio 11: POO
11.- Convierta el atributo “estado” de la 
clase Guerrero a una propiedad para que no 
pueda setearse a “defensa” cuando “estado_escudo” 
sea 0. En tal caso, deberá elevar una excepción 
ValueError, al igual que si el estado que quiere 
asignarse no es “defensa” o “ataque”.
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100
		self._estado = "ataque"
		self.estado_escudo = 100


	@property
	def is_alive(self):
		if self.vida > 0:
			return True
		else:
			return False

	@property
	def estado(self):
		if self.estado_escudo <= 0:
			self._estado = "ataque"
		return self._estado
	
	@estado.setter
	def estado(self, est):
		if self.estado_escudo <= 0:
			raise ValueError("El estado del escudo es 0")
		else:
			if est != "ataque" and est != "defensa":
				raise ValueError("El estado solo puede ser ataque o defensa")
			else:
				self._estado = est

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
print(g1.vida, g1.estado_arma, g1.estado_escudo, g1.estado)
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