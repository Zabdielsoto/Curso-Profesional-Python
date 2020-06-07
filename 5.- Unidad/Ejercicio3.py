#Ejercicio 3: Modulos

import sys

sys.path.insert(1, r"C:\python_modules\ejercicios")

import operaciones as op

ingreso = input("Ingrese numeros separados por coma: ")

valores = ingreso.split(",")
valores = [float(n) for n in valores]

s = op.suma(*valores)
r = op.resta(*valores)
m = op.producto(*valores)
d = op.division(*valores)

print("\nSuma de los numeros: ", s)
print("\nResta de los numeros: ", r)
print("\nMultiplicacion de los numeros: ", m)
print("\nDivision de los numeros: ", d)