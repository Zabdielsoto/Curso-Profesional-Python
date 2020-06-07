'''Ejercicio 7: POO
7.- Amplíe el funcionamiento del ejemplo 
anterior para que el ataque sea realizado 
únicamente si el atributo “estado_arma” de 
la clase que ejecuta el método es mayor o igual a 2.
'''

class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100

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
print("\nGuerrero 2 despues de atacar")
print(g2.vida, g2.estado_arma)