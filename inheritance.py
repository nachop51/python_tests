# ineficiente de gestionar

# class Producto:
#     def __init__(self,referencia, tipo,nombre, pvp, descripcion, productor=None, distribuidor=None, isbn=None, autor=None):
#         self.referencia = referencia
#         self.tipo = tipo
#         self.nombre = nombre
#         self.pvp = pvp
#         self.descripcion = descripcion
#         self.productor = productor
#         self.distribuidor = distribuidor
#         self.isbn = isbn
#         self.autor = autor

# adorno = Producto('0A', 'Adorno', 'Vaso decorado', 15, 'Vaso de vidrio decorado')
# print(adorno.tipo)

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

class Adorno (Producto):
    pass

a = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana adornado con árboles")
print (a)

class Alimento (Producto):
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

print(al)