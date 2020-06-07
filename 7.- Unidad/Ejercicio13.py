'''Ejercicio 13: POO
Cree una nueva clase Arma que posea los 
atributos nombre, daño y estado. El atributo 
estado debe poseer las características del 
atributo estado_arma que definimos en la clase Guerrero.
'''
class Arma:
	def __init__(self, nombre, daño):
		self.nombre = nombre
		self.daño = daño
		self.estado = 100

class Guerrero:
	def __init__(self, arma):
		self.vida = 100
		self._estado = "ataque"
		self.estado_escudo = 100
		self.arma = arma


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
		if guerr.is_alive == True:
			if self.estado == "ataque":
				if self.estado_arma >= 2:
					if guerr.estado == "ataque":
						guerr.vida -= 20
						self.estado_arma -= 2
					elif guerr.estado == "defensa":
						guerr.estado_escudo -= 5
						self.estado_arma -= 2
				else:
					print("El arma no tiene suficiente poder")
			else:
				print("Se tiene que estar en estado de ataque")
		else: 
			print("El objetivo ya esta muerto")
