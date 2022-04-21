from tkinter import *

root = Tk()
root.title("Mi ventanita")
root.iconbitmap("favicon.ico")
root.resizable(True, True)

frame = Frame(root)
frame.pack(fill="both", expand=1)
frame.config(width=800, height=600, cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="flat")

root.config(cursor="arrow")
root.config(bg="violet")
root.config(bd=5)
root.config(relief="flat")

root.mainloop()