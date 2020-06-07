'''Ejercicio 6: Diccionarios
6.- Agregue la pareja Yen (¥) con el método setdefault.
'''

monedas = {'Euro': '€', 'Dolar': '$'}
print("Diccionario Original\n",monedas)

monedas.setdefault("Yen", '#')
print("\nDiccionario Modificado\n", monedas)