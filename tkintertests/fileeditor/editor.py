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
    path = FileDialog.askopenfilename(initialdir=".", filetype=(("Text files", "*.txt"),("All","*.*")), title="Open a file")
    if path != "":
        file = open(path, "r")
        contenido = file.read()
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        file.close()
        root.title(path + " - Nachecker Studio Code")
        msg.set(f"File {path} successfully opened")

def save():
    global path
    msg.set("Save")
    if path != "":
        contenido = texto.get(1.0, "end-1c")
        file = open(path, "w+")
        file.write(contenido)
        file.close()
        msg.set(f"Saved at {path}")
    else:
        saveas()

def saveas():
    global path
    msg.set("Save As...")
    file = FileDialog.asksaveasfile(title="Save As", mode="w", defaultextension=".txt")
    if file is not None:
        path = file.name
        contenido = texto.get(1.0, "end-1c")
        file = open(path, "w+")
        file.write(contenido)
        file.close()
        msg.set(f"Saved at {path}")
    else:
        msg.set("Save failed")
        path = ""

root = Tk()
root.title("Nachecker Studio Code")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New file", command=newfile)
filemenu.add_command(label="Open file...", command=openfile)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As...", command=saveas)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
filemenu.config(bg="#21252B", fg="#D7DAE0")

menubar.add_cascade(menu=filemenu, label="File")

# Espacio para escribir
texto= Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=5, pady=5, font=("Consolas", 12))
texto.config(selectbackground="#404859", bg="#282C34", fg="#CCCCCC", insertbackground="#528BFF", insertwidth=2)

# Monitor inferior
msg = StringVar()
msg.set("Welcome to Nachecker Studio Code")
monitor = Label(root, textvar=msg, justify="left")
monitor.pack(side="left")

root.config(menu=menubar, relief="groove")
root.mainloop()