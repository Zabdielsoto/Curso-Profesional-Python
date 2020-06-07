'''Ejercicio 6: Clases
6.- Modifique el método anterior para que, 
además de disminuir el atributo “vida” de 
la instancia recibida, disminuya en 2 el 
atributo “estado_arma” del objeto que ejecuta 
el método.
'''
class Guerrero:
	def __init__(self):
		self.vida = 100
		self.estado_arma = 100

	def atacar(self, guerr):
		guerr.vida -= 20
		self.estado_arma -= 2


g1 = Guerrero()
g2 = Guerrero()

print("Guerrero 1 sin haber sido atacado")
print(g1.vida, g1.estado_arma)
print("\nGuerrero 2 antes de atacar")
print(g2.vida, g2.estado_arma)
g2.atacar(g1)
print("\nGuerrero 1 despues de haber sido atacado")
print(g1.vida, g1.estado_arma)
print("\nGuerrero 2 despues de atacar")
print(g2.vida, g2.estado_arma)