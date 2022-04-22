from tkinter import *

def seleccionar():
    monitor.config(text=f"{opcion.get()}")
# con esto podemos ver el valor del boton en una label y actualizarla dinamicamente

def reset():
    opcion.set(None)
    monitor.config(text="")
# al setear nuestra variable en None estamos borrando la seleccion que hicimos

root = Tk()
# IntVar() nos permite guardar un valor que despues podemos consultar o borrar
opcion = IntVar()
# Radiobutton crea los botones de valor unico
# es necesario pasarle un value, para que todos sean distinguibles
# en variable=x es donde guardamos el valor
Radiobutton(root, text="Opcion 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text="Opcion 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text="Opcion 3", variable=opcion, value=3, command=seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()