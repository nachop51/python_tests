from tkinter import *

root = Tk()
# con la funcion PhotoImage, especificando la ruta del archivo con file="name.png"
# podemos mostrar una foto en pantalla de la siguiente manera
imagen = PhotoImage(file='pikachu.png')
Label(root, image=imagen, bd=0).pack()

root.mainloop()
