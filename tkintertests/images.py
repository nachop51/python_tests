from tkinter import *

root = Tk()

imagen = PhotoImage(file='pikachu.png')
Label(root, image=imagen, bd=0).pack()

root.mainloop()
