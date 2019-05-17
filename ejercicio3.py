from tkinter import *
#definicion de clase App y sus miembros.
class App:
#miemros de App
	def __init__(self, master):
		#instancia de widget frame, cuyo contenedor debe ser enviadoo como argumento
		frame = Frame(master)
		#organizacion en bloques
		frame.pack()
		#instancia de boton			
		self.button = Button(frame, text="SALIR", fg="red",command=frame.quit)
		self.button.pack(side=LEFT)
		self.slogan = Button(frame,text="ENTRAR",command=self.write_slogan)
		self.slogan.pack(side=LEFT)

	def write_slogan(self):
		print ("Estamos aprendiendo a usar Tkinter!")
		

#crea instancia de "App"
root=Tk()

ejemplo=App(root)
root.mainloop()