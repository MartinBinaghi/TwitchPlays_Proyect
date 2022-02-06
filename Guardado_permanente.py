import pickle

class Persona():

	def __init__(self, nombre, edad, Lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.Lugar_residencia=Lugar_residencia
		print("Se ha creado una persona con el nombre de",self.nombre)

	def descripcion(self):
		print("Nombre: ", self.nombre, " Edad: ", self.edad, "Residencia: ", self.Lugar_residencia)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.edad, self.Lugar_residencia)

class ListaPersonas:
	personas=[]

	def __init__(self):
		listaDePersonas=open("ficheroExterno", "ab+")
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

		except:
			print("El fichero está vacío")

		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonas()

	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonas(self):
		listaDePersonas=open("ficheroExterno", "wb")
		pickle.dump(self.personas, listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)

	def mostrarInfoFichero(self):
		print("La informacion del fichero es la siguiente:")
		for p in self.personas:
			print(p)

miLista=ListaPersonas()

#p=Persona("Martin","20","Cordoba")
#miLista.agregarPersonas(p)

#p=Persona("Santiago","23","Cordoba")
#miLista.agregarPersonas(p)

#p=Persona("Julieta","16","Cordoba")
#miLista.agregarPersonas(p)

#ListaPersonas.mostrarPersonas(miLista)
persona=Persona("Martin", "20", "Cordoba")
miLista.agregarPersonas(persona)
miLista.mostrarInfoFichero()