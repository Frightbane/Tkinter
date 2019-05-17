from tkinter import *
#instancia
root = Tk()
#instancia de self variable
v = IntVar()
#metodo constructor concatenado al geometrico organizador
Label(root, text="""Choose a programming language:""",justify = LEFT,padx = 20).pack()
#constructr de radio button
Radiobutton(root, text="Python",padx = 20, variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Perl",padx = 20, variable=v, value=2).pack(anchor=W)
#no cerrar pantalla
mainloop()