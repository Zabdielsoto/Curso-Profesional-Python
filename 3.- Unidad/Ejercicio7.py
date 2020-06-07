'''Ejercicio 7: Diccionarios
7.- Cree un diccionario con las claves 
“buen”, “día”, “noche”, “gracias” y “hola” 
con sus respectivas traducciones al inglés 
como clave. Luego, con la frase “Hola buen día”, 
muestre su traducción obteniendo la misma 
de este diccionario.
'''
#Creamos el diccionario
dicc = {"buen" : "good", "dia" : "day", "noche" : "night",
		"gracias" : "thanks", "hola" : "hello"}
#Creamos la cadena
cadena = "hola buen dia"
#Creamos lista dividiendo las palabras
#de la cadena cada una en un elemento de la lista
lista = cadena.split()
#Lista vacia
trad = []

#Recorremos todos los elementos de la lista
for n in lista:
	#Obtenemos el valor que se encuentra en el diccionario y
	#que corresponde a la clave dada por n (el elemento de la
	# lista)
	valor = dicc.get(n)
	#Agregamos el valor dado a la nueva lista
	trad.append(valor)
#Creamos una cadena uniendo los elementos de la lista usando 
#el caracer espacio como union
final = " ".join(trad)

print("Traduccion: " + final)