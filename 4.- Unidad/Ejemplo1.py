''' Ejemplo 1: Funciones
Funciones con argumentos variables
'''

def suma(*args):
	num = 0
	for n in  args:
		num += n
	return num

def multiplicacion(*args):
	num = 1
	for n in args:
		num *= n
	return num

OPERACIONES = {
	"suma" : suma,
	"multiplicacion" : multiplicacion,
}

def operacion(*args, **kwargs):
	funcion = kwargs.get("operacion")
	op = OPERACIONES.get(funcion)
	return op(*args)

s = operacion(2, 3, 4, operacion = "suma")
print("Suma: ", s)

m = operacion(2, 3, 4, operacion = "multiplicacion")
print("\nMultiplicacion: ", m)
