from tkinter import *

root = Tk()
# la funcion grid nos permite hace una especie de "cuadrilla"
# indicando posiciones con row y column
label = Label(root, text="Nombre")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
# Entry() es el metodo para crear campos de texto para que el usuario escriba
entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
# entry.config(justify="center", state="disabled")
# con justify podemos indicar a donde queremos ubicar el texto que se escriba, y con state podemos indicar un estado
# como disabled o normal, para permitir o no escribir al usuario
label2 = Label(root, text="Apellido")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)
# tambien con padx y pady indicamos cuanto padding, es decir cuanto espaciado queremos dejar entre campos
entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
# entry.config(show="*")
# tambien podemos ocultar lo que el usuario esta escribiendo con show="*"
# este ejemplo sirve como para un campo que pida una contraseña

root.mainloop()