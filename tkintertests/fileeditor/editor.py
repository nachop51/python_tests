from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

path = "" # Va a guardar la ruta de un fichero

def newfile():
    global path
    msg.set("New file")
    path = ""
    texto.delete(1.0, "end")
    root.title("nachecker")

def openfile():
    global path
    msg.set("Open file...")
    path = FileDialog.askopenfilename(initialdir=".", filetype=(("Text files", "*.txt"),), title="Open a file")
    if path != "":
        file = open(path, "r")
        contenido = file.read()
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        file.close()
        root.title(path + " - nachecker")
        msg.set(f"File {path} open")

def save():
    msg.set("Save")
    if path != "":
        contenido = texto.get(1.0, "end-1c")
        file = open(path, "w+")
        file.write(contenido)
        file.close()
        msg.set(f"Saved at {path}")

def saveas():
    msg.set("Save As...")

root = Tk()
root.title("nachecker")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New file", command=newfile)
filemenu.add_command(label="Open file...", command=openfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As...", command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

menubar.add_cascade(menu=filemenu, label="File")

# Espacio para escribir
texto= Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=5, pady=5, font=("Consolas", 12))

# Monitor inferior
msg = StringVar()
msg.set("Welcome to nachecker")
monitor = Label(root, textvar=msg, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)
root.mainloop()