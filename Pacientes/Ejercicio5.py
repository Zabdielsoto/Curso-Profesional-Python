'''Ejercicio 5: Ficheros
5.- Cree un nuevo programa que tome los 
archivos “pacientes.pickle” y “pacientes.json”, 
los de-serialice con el módulo correspondiente 
y los guarde en un diccionario “data_pickle” y 
“data_json” respectivamente.
En el caso del módulo json, considere crear los 
objetos al momento de leerlos. 
** Ambos diccionarios creados deben dar 
True al evaluar igualdad (data_json == data_pickle)
'''

import paciente, pickle, json

with open("pacientes.pickle", "rb") as pick:
	data_pickle = pickle.load(pick)

	#print(type(data_pickle[1]))
	for n in data_pickle:
		print(data_pickle[n].id)
		print(data_pickle[n].nombre)
		print(data_pickle[n].apellido)
		print(data_pickle[n].edad)
		print(data_pickle[n].diabetico)
		print(data_pickle[n].es_diabetico)
		print("\n")

def from_json(j_object):
	if '__class__' in j_object:
		if j_object['__class__'] == 'paciente.Paciente':
			return paciente.Paciente(**j_object['__vaue__'])
	else:
		return j_object

with open("personas.json", encoding="utf-8") as j:
	data_json = json.load(j, object_hook = from_json)

	#print(data_json)
	for n in data_json:
		print(data_json[n])
		#print(data_json[n].id)
		#print(data_json[n].nombre)
		#print(data_json[n].apellido)
		#print(data_json[n].edad)
		#print(data_json[n].diabetico)
		#print(data_json[n].es_diabetico)
		print("\n")

	#print(type(data_json["1"]))
