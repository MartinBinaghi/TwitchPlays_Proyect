from tkinter import *

##############Raiz################

raiz=Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1, 1) #Habilita el cambio de tamaño

raiz.iconbitmap("rebord2.ico")

raiz.geometry("650x500")

raiz.config(bg="grey")

##############Frame################

miFrame=Frame()

miFrame.pack(fill="y", expand="1")

miFrame.config(bg="white")

miFrame.config(width="550", height="400")

##############Label################

miLabel=Label(miFrame, text="No se")

#miLabel.place(x=100, y=100)

miLabel.grid(row=0, column=0)


##############Entry################

cuadroTexto=Entry(miFrame)

cuadroTexto.grid(row=0, column=1, sticky="e", padx="100")

###################################

raiz.mainloop() #Siempre al final



