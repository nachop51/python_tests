# estas funciones adentro de la clase son metodos
# y chocolate vendria a ser un atributo de la clase

class Galleta:
    chocolate = False
    def __init__(self, sabor=None, color=None):
        # init hace el print solo cuando se crea una galleta
        self.sabor = sabor
        self.color = color
        if sabor is not None and color is not None:
            print(f"Se hizo una galleta {sabor} y {color}")
    def ponerChocolate(self):
        self.chocolate = True
    def tieneChocolate(self):
        if(self.chocolate):
            print("Tiene")
        else:
            print("No tiene")

g = Galleta("dulce", "marron")
g.tieneChocolate()
g.ponerChocolate()
g.tieneChocolate()