from tkinter import *
root = Tk() #Inicializacion del  tcl/tk interpreter y la ventana contenedora principal
etiqueta1= Label(root, text="Hello Tkinter!")#Crea instancia de widget Label
etiqueta1.pack() #organiza los widgets en bloques antes de ponerlos en el contenedor
root.mainloop()  #funcion rudimenta que evita el cierre inmediato de la ventana principal 