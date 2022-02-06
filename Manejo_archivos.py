from io import open

archivo_texto=open("archivo.txt","r")   #tambien se puede abrir en lectura y append (r)
										#'r+' lectura + escritura
##### esto para 'w'
#frase="lalalala texto de pruba \n texto abajo" 

#archivo_texto.write(frase)
#####

##### esto para 'r'
texto=archivo_texto.read()  #tambien existe el .readlines() que archiva la informacion en listas
#####						#Ademas se puede poner un caracter entre los parentesis para señalar hasta donde va a leer

##### esto para 'a' (agrega informacion)
#archivo_texto.write("\n no se")
#####

print(texto)

#################Capitulo 2###################

archivo_texto.seek(len(texto) / 2) #acomoda el puntero en un caracter

archivo_texto.close()