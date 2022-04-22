from tkinter import *

# cabe destacar que la funcion tiene que estar declarada antes
# de ser llamada por el boton
# def hola():
#     print("Hola mundo")

# def crear_label():
#     Label(root, text="Label creada de forma dinamica").pack()

def sumar():
    resultado.set(float(n1.get()) + float(n2.get()))
    borrar()

def resta():
    resultado.set(float(n1.get()) - float(n2.get()))
    borrar()

def producto():
    resultado.set(float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

# con la funcion set podemos modificar el contenido de un Entry a lo que queramos
# y con la funcion get podemos obtener lo que esta escrito en el Entry al momento de tocar el boton

root = Tk()
# Button() sirve para crear un boton en pantalla
# button = Button(root, text="Click me", command=crear_label)
# con commando podemos hacer que este boton llame a una funcion
# button.pack()

root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
resultado = StringVar()

Label(root, text="Numero 1:").pack()
Entry(root, justify="center", textvariable=n1).pack() # primer numero
Label(root, text="Numero 2:").pack()
Entry(root, justify="center", textvariable=n2).pack() # segundo numero
Label(root, text="\nResultado:").pack()
Entry(root, justify="center", textvariable=resultado, state="disabled").pack() # resultado
Label(root, text=" ").pack()
Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Resta", command=resta).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")
# side es una propiedad del pack que alinea items

root.mainloop()