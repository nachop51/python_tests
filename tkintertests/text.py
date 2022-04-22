from tkinter import *

root = Tk()

# Text() funciona como entry pero a mayor escala
texto = Text(root)
texto.pack()
# cuando usamos config width y height en un objeto tipo Text()
# no nos estamos refiriendo a pixeles cuando indicamos un numero
# si no que nos estamos refiriendo a caracteres
texto.config(width=30, height=10)
texto.config(font=("Consolas", 12), padx=5, pady=5)
texto.config(selectbackground="violet")
# con selectbackground podemos indicar que color le queremos dar
# al texto seleccionado por el usuario

root.mainloop()