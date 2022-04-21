from tkinter import *

root = Tk()

text = StringVar()
text.set("Some text right here")

frame = Frame(root, width=600, height=480)
frame.pack(fill="both", expand=1)
root.config(cursor="arrow")
root.config(bg="violet")
root.config(bd=5)
root.config(relief="flat")

# el orden de los packs afecta
Label(frame, text="Hey there!").place(x=0, y=0)
label = Label(frame)
label.place(x=400, y=400)
label.config(bg="gray", fg="white", font=("Times New Roman", 12))
label.config(textvariable=text)

root.mainloop()

