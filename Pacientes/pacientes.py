'''Ejercicio 1: Ficheros
.- Cree una clase Paciente que herede de 
collections.namedtuple con los atributos 
id, nombre, apellido, edad y diabético. 
Además, agregue la property “es_diabetico” 
que deberá devolver True si el valor del 
atributo “diabético” es “Sí”. ** Guarde 
el código en un archivo “pacientes.py”
'''

from collections import namedtuple

_Paciente = namedtuple("_Paciente", "id nombre apellido edad diabetico")

class Paciente(_Paciente):

	@property
	def es_diabetico(self):
		if self.diabetico == "Si":
			return True
		else: 
			return False

#p = Paciente(1, "Zab", "Soto", 23, "Si")
#print(p.es_diabetico)