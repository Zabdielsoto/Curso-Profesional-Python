''' Proyecto Final: Calendario Personal'''

## Modulos a importar ##
import datetime as dt
import sqlite3

##Constantes a usar en el Programa##
#Archivo de base de Datos
DB_NAME = "calendar.sqlite3"
#Objeto conexion para la base de datos
DB_CONN = sqlite3.connect(DB_NAME)

def close_conn(conexion = DB_CONN):
	''' Funcion para cerrar la conexion a una base de datos

	Parametros:
	Solo ocupa una parametro de tipo conexion (sqlite3.Connection)
	'''

	conexion.close()

def iniciar_bbdd():
	'''Funcion para crearlas tablas de la base de datos que se
	usan para guardar los eventos y asistentes en caso de que no
	existan 
	'''
	#Creamos un ojeto cursor asociado con el objeto conexion
	cursor = DB_CONN.cursor()

	#Pasamos sentencias de SQLITE con el metodo execute
	cursor.execute('''
		CREATE TABLE if not exists eventos (
		pk integer PRIMARY KEY AUTOINCREMENT,
		titulo text,
		ubicacion text,
		inicio datetime,
		fin datetime,
		descripcion text
		)'''
	)

	cursor.execute('''
		CREATE TABLE if not exists asistentes(
		pk integer PRIMARY KEY AUTOINCREMENT,
		mail text,
		evento INTEGER REFERENCES evento(pk) ON DELETE CASCADE ON UPDATE CASCADE)
		)'''
	)

	cursor.close()

#Creamos la clase Evento
class Evento:
	''' Datos de un Evento.Los objetos se guardan en la base 
	de datos '''

	def __init__ (self, titulo, pk = None, ubicacion = "", inicio = dt.datetime.now(), fin = dt.datetime.now(), descripcion = "", asistentes = []):

		self.pk = pk
		self.titulo = titulo
		self.ubicacion = ubicacion
		self.inicio = inicio if isinstance(inicio, dt.datetime) else dt.datetime.fromisoformat(inicio)
		self.fin = fin if isinstance(fin, dt.datetime) else dt.datetime.fromisoformat(fin)
		self.descripcion = descripcion
		self.asistentes = asistentes

	def __str__(self):
		