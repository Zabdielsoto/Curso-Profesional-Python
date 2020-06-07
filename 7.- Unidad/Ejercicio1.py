'''Ejercicio 1: Clases
1.- Cree una clase Punto que reciba las 
coordenadas (x, y) y un método que indique 
a qué cuadrante pertenece.
'''

class Punto:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def cuadrante(self):
		if self.x > 0 and self.y > 0:
			print("Primer cuadrante")
		elif self.x < 0 and self.y > 0:
			print("Segundo Cuadrante")
		elif self.x > 0 and self.y < 0:
			print("Tercer Cuadrante")
		elif self.x < 0 and self.y < 0:
			print("Cuarto Cuadrante")


p1 = Punto(1,1)
p2 = Punto(-1,1)
p3 = Punto(1,-1)
p4 = Punto(-1,-1)

p1.cuadrante()
p2.cuadrante()
p3.cuadrante()
p4.cuadrante()
