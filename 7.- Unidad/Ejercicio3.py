'''Ejercicio 3: Clases
3.- Cree una clase Vector que reciba 
2 instancias de la clase Punto y devuelva 
el vector resultante. Deberá poseer 3 atributos:

a: será el punto 1.
b: será el punto 2
c: @property ab: será una tupla del vector 
resultante que indicará la diferencia (distancia) 
entre los puntos recibidos.
'''
from math import sqrt as raiz

class Punto:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Vector:
	def __init__(self, punto1, punto2):
		self.a = punto1
		self.b = punto2

	def vec(self):
		v = [(self.a.x - self.b.x), (self.a.y - self.b.y)]
		return v

	@property
	def ab(self):
		v = self.vec()
		d = raiz(v[0] ** 2 + v[1] ** 2)
		return d

p1 = Punto(1, 2)
p2 = Punto(3, 4)

v1 = Vector(p1, p2)

#print(v1.vec())
print("Vector: ", v1.vec())
print("Distancia: ", v1.ab)