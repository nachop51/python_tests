from tkinter import *

def seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += "con leche"
    else:
        cadena += "sin leche"
    if (azucar.get()):
        cadena += " y con azucar"
    else:
        cadena += " y sin azucar"
    monitor.config(text=cadena)

root = Tk()
root.title("Cafeteria")
root.config(bd=15)

leche = IntVar()  # 1 si, 0 no
azucar = IntVar() # 1 si, 0 no

imagen = PhotoImage(file="cafe.gif")
# con zoom y subsample hacemos un resize de la imagen
# paso de ser de 400x400 a 100x100
imagen = imagen.zoom(10)
imagen = imagen.subsample(40)
Label(root, image=imagen, width=100, height=100).pack(side="left")

frame = Frame(root)
frame.pack(side="left")
Label(frame, text="Como queres el cafe?").pack(anchor="w")
# Checkbutton() nos facilita hacer una especie de opcion multiple, con botones que podemos marcar
# y desmarcar, para esto usamos onvalue y offvalue que sirven para indicar un valor cuando estan
# seleccionados o no
Checkbutton(frame, text="miti miti", variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="dulce", variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

root.mainloop()