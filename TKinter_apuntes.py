from tkinter import *

"""ventanas"""


Ventana=Tk()#crear ventana

# Ventana.title("prueba")#titulo
# Ventana.iconbitmap("imagenes/PruebaTK.ico")#cambiar logo en el titulo (necesita un archivo .ico)

# # Ventana.resizable(0,1)#permiso para editar el tamaño de ventana desde el programa (X,Y)
# Ventana.geometry("600x600")#editar tamaño inicial de la ventana (X x Y). Si no se agrega, la ventana toma el tamaño del frame

# Ventana.config(bg="blue")#cambiar el color de fondo de la ventana

"""frames"""

# frame1=Frame()#crear frame
# frame1.pack()#agregar el frame a la ventana. 
# #si dentro del () se agrega side= se puede anclar el frame a un lado especifico ("left", "rigth","top","bottom")
# #se luego del side=, se agrega un anchor= se puede establecer una esquina (n,s,e,w)
# #si se escribe fill= se puede hacer que el frame adopte el tamaño de la ventana todo el tiempo (x,y,both,none)
# #para que se expanda sobre el eje y se debe agregar el atributo expand=True

# frame1.config(bg="red")#cambiar color del frame
# frame1.config(width=400,height=400)#cambiar tamaño (X,Y)
# frame1.config(relief="groove")#cambiar color del borde
# frame1.config(bd=5)#establece el tamaño del borde
# frame1.config(cursor="pirate")#cambia el cuerosr en el frame
# frame1.pack_propagate(False)
# frame1.grid_propagate(False)


"""Labels"""
# label1 = Label(frame1,text="¡Hola Mundo!",bg="red")
# label1.config(height=5,width=10)
# # label1.grid(column=0,row=0)
# label1.pack(side=RIGHT)
# # label1.place(x=0,y=0)

# label2 = Label(Ventana,text="¡Hola Mundo!",bg="green",height=100,width=100)
# label2.config(height=1,width=10)
# label2.grid(column=1,row=1)
# label2.pack()
# label2.place(x=0,y=200)

# label3 = Label(Ventana,text="¡Hola Mundo!",bg="yellow")
# label3.config(height=1,width=18)
# # label3.grid(column=0,row=0)
# # # label3.config(text="Adios mundo cruel")
# label3.pack()


# label4 = Label(Ventana,text="¡Hola Mundo!",bg="yellow")
# label4.config(height=1,width=50)
# label4.grid(column=0,row=1)
# label4.pack()


"""Entry"""
# Entry1=Entry(Ventana,text="¡Hola Mundo!",bg="white")
# # entry.grid(column=0,row=1)
# Entry1.pack()

# def ejemplo():
#     # textoDeLaEntry=Entry1.get()
#     # label3.config(text=textoDeLaEntry)
#     frame1.destroy()

"""Buttons"""

# button=Button(Ventana,text="chau",command=ejemplo)
# # button.grid(column=4,row=4)
# button.pack()

"""Imgenes"""

# imagen=PhotoImage(file=r"Imagenes\PruebaTK.png")
# imagen.width()
# ImagenMostrar=Label(Ventana,image=imagen)
# ImagenMostrar.config(width=500,height=500)
# ImagenMostrar.pack()






Ventana.mainloop()#bucle para inicializar una ventana