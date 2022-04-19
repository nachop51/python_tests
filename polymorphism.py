from math import prod


class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
    def __str__(self):
        return """
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}""". format (self.referencia, self.nombre, self.pvp, self.descripcion)

class Adorno(Producto):
    pass

a = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana adornado con árboles")

class Alimento(Producto):
    productor = ""
    distribuidor = ""
    def __str__(self):
        return """
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
PRODCUTOR\t{}
DISTRIBUTOR\t{}""". format (self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)

al = Alimento(2035, "Botella de aceite de oliva extra", 5, "250ml")
al.productor = "La aceitera"
al.distribuidor = "Distribuidor"

class Libro(Producto):
    isbn = ""
    autor = ""
    def __str__(self):
        return """
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
ISBN\n\t{}
AUTOR\n\t{}""". format (self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)

li = Libro("2036", "Harringy Potter", 20, "Libro de harry")
li.isbn = "123123"
li.autor = "JK"

productos = [a, al]
productos.append(li)
# for p in productos:
#     # print(p,"\n")
#     print(p.referencia, p.nombre)

# isinstance se fija si el objeto pertenece al segundo parametro y devuelve ToF
for p in productos:
    if(isinstance(p, Adorno)):
        print(p.referencia,p.nombre)
    elif(isinstance(p, Alimento)):
        print(p.referencia,p.nombre, p.productor, p.pvp)
    elif(isinstance(p, Libro)):
        print(p.referencia,p.nombre,p.isbn)

def rebajar_producto(p, rebaja):
    """Devuelve un producto con una rebaja en porcentaje de su precio"""
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

rebajar_producto(al, 10)
print(al)

# a tener en cuenta, los objetos se pasan por puntero a la memoria, para poder hacer una copia
# es necesario importart un nuevo modulo --> copy, funciona asi
# import copy
# copia = copy.copy(al)
# la modificacion de esta copia no afecta a la original
# mientras que si modificamos como normalmente hariamos una copia, por referncia
# si modificaria el original