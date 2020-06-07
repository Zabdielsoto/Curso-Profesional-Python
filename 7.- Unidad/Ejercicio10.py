'''Ejercicio 10: POO
10.- Cree una nuevo atributo “estado_escudo” 
a la clase Guerrero, que se inicialice en 100 por defecto.
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100
		self.estado = "ataque"
		self.estado_escudo = 100


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
print(g1.vida, g1.estado_arma, g1.estado, g1.estado_escudo)
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