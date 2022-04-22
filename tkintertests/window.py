from tkinter import *

# con Tk() creamos nuestra instancia de ventana
root = Tk()
# con .title() podemos ponerle un nombre a nuestra ventana
root.title("Mi ventanita")
# tambien podemos cambiarle el icono de esta forma
root.iconbitmap("favicon.ico")
# .resizable() nos permite indicarle a la ventana si queremos que se pueda cambiar su tamaño o no
root.resizable(True, True)

# con Frame() creamos una instancia dentro de la ventana, para que no afecte a la principal
frame = Frame(root)
# la funcion pack si no indicamos parametros lo que hace es hacer un resize de la ventana
# a que ocupe solo el tamaño necesario para lo que se esta mostrando
# fill="both" y expand=1 le indica al frame que siga al tamaño de root
frame.pack(fill="both", expand=1)
# y con config, podemos modificar este frame a nuestro gusto, por ejemplo
# con width y height, especificamos ancho y alto de la ventana
# y con cursor, cambiamos el cursor que se muestra cuando el mouse esta posado en la ventana
frame.config(width=800, height=600, cursor="pirate")
# con bg podemos cambiar el fondo
frame.config(bg="lightblue")
# con bd podemos indicar el ancho del border que pongamos
frame.config(bd=25)
# relief sirve para indicar que tipo de borde queremos agregar a nuesta ventana
frame.config(relief="flat")

root.config(cursor="arrow")
root.config(bg="violet")
root.config(bd=5)
root.config(relief="flat")

root.mainloop()