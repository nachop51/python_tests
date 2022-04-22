from tkinter import *

root = Tk()
# con StringVar podemos declarar texto para usarlo en labels
# la ventaja de tener el texto aca, es que despues puede ser modificado
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
# la funcion place nos permite ubicar algo en una determinada posicion de la ventana
label.place(x=400, y=400)
# con font y una tupla, podemos especificar la fuente que queremos usar y el tamaño de la fuente en px
label.config(bg="gray", fg="white", font=("Times New Roman", 12))
# aqui vendria la variable StringVar que declaramos arriba
label.config(textvariable=text)

root.mainloop()

