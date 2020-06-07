'''Ejercicio 16: POO
Modifique el método atacar y la property 
estado de la clase Guerrero para que considere 
los cambios realizados en el punto anterior.
'''

class Escudo:
	def __init__(self, nombre, absorcion):
		self.nombre = nombre
		self.absorcion = 10
		self.estado = 100

class Arma:
	def __init__(self, nombre, daño):
		self.nombre = nombre
		self.daño = daño
		self.estado = 100

class Guerrero:
	def __init__(self, arma, escudo):
		self.vida = 100
		self._estado = "ataque"
		self.escudo = escudo
		self.arma = arma


	@property
	def is_alive(self):
		if self.vida > 0:
			return True
		else:
			return False

	@property
	def estado(self):
		if self.escudo.estado <= 0:
			self._estado = "ataque"
		return self._estado
	
	@estado.setter
	def estado(self, est):
		if self.escudo.estado <= 0:
			raise ValueError("El estado del escudo es 0")
		else:
			if est != "ataque" and est != "defensa":
				raise ValueError("El estado solo puede ser ataque o defensa")
			else:
				self._estado = est

	def atacar(self, guerr):
		if guerr.is_alive == True:
			if self.estado == "ataque":
				if self.arma.estado >= 2:
					if guerr.estado == "ataque":
						guerr.vida -= 20
						self.arma.estado -= 2
					elif guerr.estado == "defensa":
						guerr.escudo.estado -= 5
						self.arma.estado -= 2
				else:
					print("El arma no tiene suficiente poder")
			else:
				print("Se tiene que estar en estado de ataque")
		else: 
			print("El objetivo ya esta muerto")