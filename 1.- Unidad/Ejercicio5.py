'''Ejercicio Propuesto 5: Tipos de Datos

Cree un programa que almacene en variables 
los conjuntos {1,5,7,3,4,2} y {1,4,9,15,21} e indique:
La intersección entre ambas variables 
(valores que se encuentran en ambas variables).

Los valores que se encuentran en cualquiera de los dos 
conjuntos pero no en ambos a la vez.
'''

conjunto1 = {1, 5, 7, 3, 4, 2}
conjunto2 = {1, 4, 9, 15, 21}
print("Conjunto 1: ", conjunto1)
print("Conunto 2: ", conjunto2, "\n")
print("Interseccion de los dos conjuntos")
print(conjunto1 & conjunto2, "\n")

print("Valores que no estan en los dos conjuntos a la vez")
print(conjunto1 ^ conjunto2)