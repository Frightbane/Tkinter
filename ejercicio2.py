from tkinter import *
#instancia de contenedor principal
master = Tk()
#string con mensaje
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
#instancia de widget message
msg = Message(master, text = whatever_you_do)
#cambia parametros mediante el metodo config presente en varios widgets de tkinter
msg.config(bg='lightgreen',font=('times', 24, 'italic'))
#organiza en bloques
msg.pack( )
#impide el cierre del programa
mainloop( )