import re
from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()

def test():
    # MessageBox.showinfo("Hi there!","This is a test")
    # MessageBox.showwarning("Alert!","You are not allowed to do this")
    # MessageBox.showerror("Error!","An unexpected error occurred")
    # result = MessageBox.askquestion("Quit","Quit without saving?") # devuelve "yes" o "no"
    # if result == "yes":
    #     root.destroy()
    # result = MessageBox.askokcancel("Quit","Overwrite current file?") # devuelve True or false
    # if result:
    #    root.destroy()
    # result = MessageBox.askyesno("Quit","Quit without saving?") # devuelve true or false
    # if result:
    #     root.destroy()
    result = MessageBox.askretrycancel("Retry","Can't connect to the server") # devuelve true or false
    if result:
        root.destroy()

Button(root, text="Click me", command=test).pack()

root.mainloop()