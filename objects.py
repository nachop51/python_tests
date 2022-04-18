# Ejemplo de implementación con Programación Estructurada

# clientes = [
#     {'Nombre': 'Hector', 'Apellidos': 'Costa Guzman', 'dni': '11111111A'},
#     {'Nombre': 'Juan', 'Apellidos': 'González Márquez', 'dni': '22222222B'}
# ]

# def mostrar_cliente(clientes, dni):
#     for c in clientes:
#         if (dni == c['dni']):
#             print('{} {}'.format(c[ 'Nombre'],c['Apellidos']))
#             return
#     print('Cliente no encontrado')

# mostrar_cliente(clientes, "11111111A")

# def borrar_cliente(clientes, dni):
#     for i,c in enumerate(clientes):
#         if (dni == c['dni']):
#             del( clientes[i] )
#             print(str(c),"> BORRADO")
#             return
#     print('Cliente no encontrado')

# borrar_cliente(clientes, "11111111A")
# borrar_cliente(clientes, "11111111A")

# Con objetos

# Ejemplo de implementación con Programación Orientada a Objetos

class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
    def __str__(self):
       return '{} {}'.format(self.nombre, self.apellidos)

class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")
    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

nacho = Cliente(nombre="Nacho", apellidos="Peralta", dni="1234")
print(nacho)
juan = Cliente("222", "Juancho", "Talarga")
print(juan)
empresa = Empresa(clientes=[nacho, juan])

print(empresa.clientes)
empresa.mostrar_cliente(dni="1234")
empresa.borrar_cliente(dni="222")