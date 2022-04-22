from msilib.schema import File
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

def test():
    # con esto podemos permitir que el usuario elija un color
    # color = ColorChooser.askcolor(title="Choose a color")
    # print(color)
    # path = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", filetypes=(("Text", "*.txt"), ("All", "*.*")))
    # print(path)
    # cuidado con esto porque abre un archivo y borra el contenido xd
    # equivale por default a open("path", "w")
    path = FileDialog.asksaveasfile(title="Save a file", mode="w", defaultextension=".txt")
    print(path)
    if path is not None:
        path.write("Hola! esto esta modificado desde popups2.py de tkinterstests")
        path.close()

Button(text="Click me", command=test).pack()

root.mainloop()