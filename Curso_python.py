import math

#print("manteca")

def mi_nombre():
	print("Martin")

#mi_nombre()

def nombre_y_edad(año):
	print("mi nombre es martin y tengo "+año+" años")

#nombre_y_edad("veinte")

def multiplicacion(num1,num2):
	print(num1*num2)
	if (num1*num2 > 100):
		return ("ta grande")

#print (multiplicacion(5,100))

fromsoftware_games=["darksouls1"]										#Lista, va entre corchetes

#def agregar_a_from (game):
#fromsoftware_games.append(game)
#agregar_a_from ("darksouls2")

fromsoftware_games.extend(["darksouls2","darksouls3","elden ring"])
fromsoftware_games.insert(0, "demon´s souls")
fromsoftware_games.insert(4, "bloodborne")

#print (fromsoftware_games[0:])
#print (fromsoftware_games.index("darksouls2"))
#print ("Resident evil 4" in fromsoftware_games)

mis_perros= ("coco", "lola", "uma")										#Tupla, va entre parentesis. Son como las listas, pero no se modifican.

#print (mis_perros)
#print (mis_perros.count("coco"))
#print (len(mis_perros))

perro_viejo, perra_chillona, perra_negra=mis_perros						#A cada elemento de la tupla le pongo una variable

#print (perro_viejo, perra_chillona, perra_negra)

locaciones = ("Cordoba", "Santa fe", "Argentina")
diccionario_random={locaciones[0]:"Cordoba",locaciones[1]:"Santa fe",locaciones[2]:"CABA"}  #Diccionario {}
#print (diccionario_random["Argentina"])

diccionario_random["Perú"]="Lima"
#print (diccionario_random["Perú"])

del diccionario_random["Perú"]
#print (diccionario_random)

#print (diccionario_random.keys())
#print (diccionario_random.values())

#########################################

#print("programa de retribucion" )
#nota_alumno = input() 

#def evaluacion(nota):													#Condicionales, IF

	#valoracion="aprobado"

	#if nota>=6:															#No son necesarios ()
	#if nota<6:	
		
		#valoracion="desaprobado"
	#return valoracion

#print(evaluacion(7))

#def retribucion_evaluacion(nota):                                      #Condicional que utiliza la funcion condicional 69
	#if evaluacion(nota)=="aprobado":
		#return "bien ahi capo"
	#else:
		#return "mal ahi capo"

#print (retribucion_evaluacion(int(nota_alumno)))


def evaluacion(nota):													#Igual al programa anterior, pero un poco mas complejo, para usar elif		

	valoracion=""

	if nota>=7:															
		valoracion="promocional"
	elif nota >=4:
		valoracion="regular"
	else:
		valoracion="desaprobado"
	return valoracion

#print(evaluacion(7))

def retribucion_evaluacion(nota):                                      
	if evaluacion(nota)=="promocional":
		return "bien ahi capo"
	elif evaluacion(nota)=="regular":
		return "pasaste de ogt capo"
	else:
		return "mal ahi capo"

#print (retribucion_evaluacion(int(nota_alumno)))
#print (retribucion_evaluacion(2))

########################################

#print ("Programa de numero maximo")										#Primer ejercicio para condicionales

#numero1= input("El numero 1 es: ")
#numero2= input("El numero 2 es: ")

def Maximo_de_dos(num1,num2):											
	Numero_máximo=num1

	if num2>num1:
		Numero_máximo=num2

	return Numero_máximo
#print (Maximo_de_dos(numero1, numero2))

#########################################

#print ("Programa de datos personales")										#Segundo ejercicio de condicionales

#dato1=input("Insertar nombre: ")
#dato2=input("Insertar direccion: ")
#dato3=input("Insertar telefono: ")

def Datos_personales(nombre,direccion,tfno):
	datos_personales=[nombre,direccion,tfno]
	return "Los datos personales son: " + nombre + ", "+ direccion +", "+ tfno + "."
#print (Datos_personales(dato1, dato2, dato3))

#########################################

#print ("programa de media aritmetica")										#Tercer ejercicio de condicionales

#numero1= input("El numero 1 es: ")
#numero2= input("El numero 2 es: ")
#numero3= input("El numero 3 es: ")

def Media_aritmetica(num1,num2,num3):
	Suma=num1+num2+num3
	return float(Suma/3)
#print (Media_aritmetica(numero1,numero2,numero3))

######################################### 

#Salario_jefe=int(input("Introduce saliro del jefe: "))
#print ("El salario del jefe es: " + str(Salario_jefe))

#Salario_gerente=int(input("Introduce saliro del gerente: "))
#print ("El salario del gerente es: " + str(Salario_gerente))

#Salario_obrero=int(input("Introduce saliro del obrero: "))
#print ("El salario del obrero es: " + str(Salario_obrero))

def Salario_por_puesto(jefe,gerente,obrero):
	if jefe>gerente>obrero:
		return "Los salarios estan bien"
	else:
		return "los salarios no estan bien"
#print (Salario_por_puesto(Salario_jefe,Salario_gerente,Salario_obrero))


#for i in fromsoftware_games:									#Bucle, el codigo se repite segun la cantidad de elementos contenidos en el segundo parametro, la i representa los parametros en cuestion.
	#print (i, end=", ")

#for i in range(6):                                              #"range" determina la cantidad de veces que se repite el bucle
	#print (fromsoftware_games[i])


#WHILE

#Intentos=0
#while len(fromsoftware_games)==6:                              #El while funciona como el if, recordar que hay que salir de algun modo del bucle

	#print("texto de prueba")
	#Intentos = Intentos + 1

	#if Intentos == 10:
		#print ("La lista sigue igual mostro qsy")
		#break;

#print ("programa de cálculo de raíz cuadrada")
#numero=int(input("introduce un número por favor: "))

#intentos=0

#while numero<0:
	#print ("no se puede hallar la raíz de un número negativo")

	#numero=int(input("introduce un número por favor: "))
	#if numero<0:
		#intentos = intentos+1

	#if intentos==2:
		#print("Has consumido demasiados intentos. El programa ha finalizado")
		#break;

#if intentos<2:
	#solucion=math.sqrt(numero)
	#print ("La raíz cuadrada de " + str(numero) + " es " + str(solucion))


#CONTINUE(continue)              permite saltar al proximo elemento del for/in, sin ejecutar el resto del codigo dentro del for


#nombre="Martin Binaghi"

#contador=0

#for i in nombre:

	#if i==" ":
		#continue           
	#contador+=1

#print(contador)


#PASS(pass)                   devuelve un nulo


#ELSE(else)                   es else por fuera del if, del for. No funciona como un condicional

#email=input("Introduce tu email, por favor: ")

#for i in email:

	#if i=="@":
		#arroba=True
		#break;
#else: 
	#arroba=False

#print(arroba)

###################

def generaPares(limite):						#Utilizando listas

	num=1
	miLista=[]

	while num<limite:

		miLista.append(num*2)
		num+=1

	return miLista

#print(generaPares(10))

#########Generadores 1##########								'Yield' La misma funcion anterior pero con generadores 'yield'

def producePares(tope):

	num=1
	while num<tope:

		yield num*2
		num+=1

devuelvePares=producePares(10)

#for i in devuelvePares:

	#print (i)

#print(next(devuelvePares))
#print(next(devuelvePares))
#print(next(devuelvePares))
#print(next(devuelvePares))
#print(next(devuelvePares))
#print(next(devuelvePares))
#print(next(devuelvePares))
#print(next(devuelvePares))
#print(next(devuelvePares))						#Cada next lleva al proximo valor de 'tope'

##########Generadores 2#########                'Yield from', Entra a los elementos de los elementos.

#username=input("el usuario de twitch es: ")
#nombre=[]
#abecedario=("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

#def devuelve_username(*username):

#	for elemento in username:
#		yield from elemento

#usarname_devuelto=devuelve_username(*username)

#for i in usarname_devuelto:
#	nombre.append(i)

#if abecedario[0:20].index(nombre[0]):
#	print("funciona")

#############Contador##################

#n = 0

#while n<=10:
#	print(n)
#	n=n+1
	
#############Excepciones 1##################							Forma de la excepcion, twitch template. Tambien se pueden enmarcar errores particulares

#def x:
#	try:

#	except Exception as e:
#        print("Encountered exception: " + str(e))

#############Excepciones 2##################                            Solo sale del bucle si no hay un error en el try.

#while True:

#	try:
#		xxxxx
#		xxxxx

#		break
#	except Exception as e:
#        print("Encountered exception: " + str(e))	

#	finally:															Se ejecuta aunque haya un error					
		#####					

#############Excepciones 3##################                            Producir intencionalmente excepciones

#def evaluaEdad(edad):

#	if edad<0:
#		raise ZeroDivisionError("No se puede dividir por 0")       		#Tambien pueden crearse tipos propios de error. Ejemplo 'ErrorPropio'

#	elif edad<20:
#		return "Sos muy joven"

#	elif edad<40:
#		return "Sos joven"

#	elif edad<65:
#		return "Sos viejo"

#	elif edad<100:
#		return "uff"

#print(evaluaEdad(-15))

################ POO ###################

class Auto:
	#ruedas=4  														#Estado inicial 
	#enMarcha=False													#
	#largoChasis=250												#
	#anchoChasis=120												#

	def __init__(self):
		self.__ruedas=4  											# (Constructor) determina como van a empezar cada objeto de la clase. '__' encapsula una propiedad, impidiendo que la modifiquen los objetos. 
		self.largoChasis=250											
		self.anchoChasis=120														

	#def arrancar(self, arrancamos):
	#	self.enMarcha=arrancamos
	#	chequeo=self.__chequeo_interno()

	#	if self.enMarcha:
	#		chequeo

	#	if self.enMarcha and chequeo:
	#		return "El auto ya arrancó"

	#	elif self.enMarcha and chequeo==False:
	#		return "El auto no ha podido arrancar"

	#	else: 
	#		return "El auto no arrancó"

	#def propiedades(self):
	#	print (self.__ruedas)
	#	print (self.enMarcha)
	#	print (self.largoChasis)
	#	return self.anchoChasis

	def __chequeo_interno(self):									#Tambien se pueden encapsular los metodos
		print ("Realizando chequeo interno...")

		self.gasolina = "ok"
		self.puertas_cerradas = "ok"
		self.ruedas_infladas = "ok"

		if self.gasolina == "ok" and self.puertas_cerradas == "ok" and self.ruedas_infladas == "ok":
			return True
		else:
			return False

miAuto=Auto()

#print(miAuto.chequeo_interno())
#print(miAuto.arrancar(True))
#print (miAuto.__ruedas)
#print (miAuto.enMarcha)
#print (miAuto.propiedades())

miSegundoAuto=Auto()
#print (miSegundoAuto.__ruedas)
#print (miSegundoAuto.enMarcha)

###############SuperClase###############

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
		
class Moto(Vehiculos):		#Se puede heredar de dos clases si se ponen las dos clases separadas por coma. La primera de las dos tiene prioridad en relacion al constructor.
	hac_caballito=""

	def caballito(self):
		self.hac_caballito="estoy haciendo caballito"

	def estado(self):											#Cuando hay un metodo del mismo nombre, el metodo dentro del objeto tiene prioridad
		print ("Marca; ", self.marca, "\nMotor; ", self.enMarcha, "\nModelo; ", self.modelo, "\nAcelera; ", self.acelera, "\nFrena; ", self.frena, "\nCaballito: ", self.hac_caballito)

miMoto=Moto("okinoi","2005")

#miMoto.estado()

################Super ()###################

class Persona():

	def __init__(self, nombre, edad, Lugar_residencia):

		self.nombre=nombre
		self.edad=edad
		self.Lugar_residencia=Lugar_residencia

	def descripcion(self):

		print("Nombre: ", self.nombre, " Edad: ", self.edad, "Residencia: ", self.Lugar_residencia)

class Empleado(Persona):

	def __init__(self, salario, antigüedad, nombre_empleado, antigüedad_empleado, residencia_empleado):

		super().__init__(nombre_empleado, antigüedad_empleado, residencia_empleado)  #'super().' accede al constructor de la clase padre.

		self.salario=salario
		self.antigüedad=antigüedad

Pepe=Empleado(1500, 15, "Pepe", 55, "Argentina")

#print(isinstance(Pepe, Empleado))  #Señala si el objeto es una instancia de la clase señalada.


#############Polimorfismo###############


class VehiculoRandom1():

	def desplazamiento(self):
		print("Me desplazo en dos ruedas")

class VehiculoRandom2():

	def desplazamiento(self):
		print("Me desplazo en cuatro ruedas")

class VehiculoRandom3():

	def desplazamiento(self):
		print("Me desplazo en seis ruedas")

def desplazamientoEnVehiculo(vehiculo):    #El polimorfismo tiene lugar en 'vehiculo', porque cambia de objeto
	vehiculo.desplazamiento()

miVehiculo1=VehiculoRandom1()
miVehiculo2=VehiculoRandom2()
miVehiculo3=VehiculoRandom3()

#desplazamientoEnVehiculo(miVehiculo1)
#desplazamientoEnVehiculo(miVehiculo2)
#desplazamientoEnVehiculo(miVehiculo3)


#####################Cadenas########################

#edad=input ("Introduce la edad: ")
#nombreUsuario=input("Introduce tu nombre de usuario: ")

#print ("El nombre de usuario es: ", nombreUsuario.upper())
#print ("El nombre de usuario es: ", nombreUsuario.lower())
#print ("El nombre de usuario es: ", nombreUsuario.capitalize())
#print (nombreUsuario.isdigit())

def evaluaEdad(edad):

	if int(edad)<0:
		raise ZeroDivisionError("No se puede dividir por 0")       		#Tambien pueden crearse tipos propios de error. Ejemplo 'ErrorPropio'

	elif int(edad)<20:
		return "Sos muy joven"

	elif int(edad)<40:
		return "Sos joven"

	elif int(edad)<65:
		return "Sos viejo"

	elif int(edad)<100:
		return "uff"


#while (edad.isdigit()==False):

	#print("Por favor, introduce un valor numerico")

	#edad=input("Introduce la edad: ")

#print (evaluaEdad(edad))

#################Ejercicio V.33#################


#mail=input("Introduce tu email: ")         #Asi lo hice yo, en el pdf dice de hacerlo de otra forma

#while mail.count("@")!=1 or (mail.startswith("@") or mail.endswith("@")):

#	print ("El mail introducido es erroneo")
#	mail=input("Inserte un mail valido: ")

#print ("El mail introducido es correcto")


#################Modulos#######################




