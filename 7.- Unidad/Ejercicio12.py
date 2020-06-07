'''Ejercicio 12: POO
12.- Modifique el método “atacar” de la clase 
Guerrero para que, actúe de la siguiente manera:

a: Si el “estado” de la instancia recibida es 
“defensa”, disminuya el estado del escudo en 5.

b: Si el “estado” de la instancia recibida es 
“ataque”, disminuya el estado de la vida en 20.

c: En cualquiera de los casos, dismuya en 2 el 
estado del arma que ejecuta el método.

d: Compruebe que el estado de la instancia que ejecuta 
el método sea “ataque”.

e: El ataque sea realizado únicamente si la instancia 
recibida esta viva.
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












