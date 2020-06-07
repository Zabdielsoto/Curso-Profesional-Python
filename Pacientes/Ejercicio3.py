'''Ejercicio3: Ficheros
3.- Extienda el código del ejercicio anterior 
para serializar los objetos del diccionario 
“data” con el módulo pickle. **Guarde el 
contenido como “pacientes.pickle”.
'''

import paciente, pickle
with open("pacientes.txt", "r+") as file:

	#print(file.read())
	p = file.readlines()
	p1 = []
	p2 = []

	for n in p[1:6]:
		p1.append(list(n.rstrip("\n").partition("=")))
	#print(p1)

	for n in p[8:len(p) + 1]:
		p2.append(list(n.rstrip("\n").partition("=")))
	#print(p2)
	p3 = []
	p4 = []
	
	for n in p1:
		n.remove("=")
		p3.append(n)

	#print(p3)
	for n in p2:
		n.remove("=")
		p4.append(n)
	#print(p4)

	pac1 = paciente.Paciente(int(p3[0][1]), p3[1][1].strip(" "),\
		 p3[2][1].strip(" "),int(p3[3][1]), p3[4][1].strip(" "))

	pac2 = paciente.Paciente(int(p4[0][1]), p4[1][1].strip(" "),\
		 p4[2][1].strip(" "), int(p4[3][1]), p4[4][1].strip(" "))

	data = {}
	data.update({pac1.id : pac1})
	#print(data)
	data.update({pac2.id: pac2})

	with open("pacientes.pickle", "wb") as archivo:
		pickle.dump(data, archivo)
	print(data)
	#print(type(data))
	#print(pac2.nombre, pac2.es_diabetico)