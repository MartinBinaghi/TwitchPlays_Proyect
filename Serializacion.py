import pickle

#lista_nombres=["Pedro", "Ana", "María", "Isabel"]

#fichero_binario=open("lista_nombres", "wb") #'wb' escritura binaria

#pickle.dump(lista_nombres, fichero_binario)

#fichero_binario.close()

#del (fichero_binario)

#############Esto es para abrir ese archivo#############

#fichero=open("lista_nombres", "rb")  # 'rb' lee codigo binario

#lista=pickle.load(fichero)

#print(lista)

#############Serializacion II############## (Objetos)

class Vehiculos():

	def __init__(self,marca,modelo):
		self.enMarcha=False
		self.modelo=modelo
		self.marca=marca
		self.acelera=False
		self.frena=False

	def arrancar(self, arrancamos):
		self.enMarcha=arrancamos
		chequeo=self.__chequeo_interno()

		if self.enMarcha:
			chequeo

		if self.enMarcha and chequeo:
			return "El auto ya arrancó"

		elif self.enMarcha and chequeo==False:
			return "El auto no ha podido arrancar"

		else: 
			return "El auto no arrancó"

	def acelerar(self):
		self.acelera=True

	def frena(self):
		self.frena=True

	def propiedades(self):
		print ("Marca; ", self.marca, "\nMotor; ", self.enMarcha, "\nModelo; ", self.modelo, "\nAcelera; ", self.acelera, "\nFrena; ", self.frena)

Auto1=Vehiculos("lalala", "1")
Auto2=Vehiculos("lololo", "2")
Auto3=Vehiculos("lululu", "3")

Autos=[Auto1, Auto2, Auto3]

fichero=open("losAutos", "wb")

pickle.dump(Autos, fichero)

fichero.close()

del (fichero)

ficheroApertura=open("losAutos", "rb")

misAutos=pickle.load(ficheroApertura)

ficheroApertura.close()

for a in misAutos:

	print(a.propiedades())