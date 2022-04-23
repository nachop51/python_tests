lista = [1, 2, 3, 4, 5]

def hola():
    numero = 10
    def bienvenido ():
        return "Hola!"
    # con esta funcion podemos ver en un diccionario todo lo declarado local
    # adentro de esta funcion "hola"
    # print(locals())
    # global nos muestra todo lo declarado
    # print(globals())
    return bienvenido
# print(hola())
# print(globals().keys())
# desde el diccionario globals podemos ver la lista declarada antes
# print(globals()["lista"])

# con esto estamos ejecutando la funcion hola, y despues la de bienvenido
print(hola()())

# tambien podemos asignar la funcion a una variable
bienvenido = hola()
print(bienvenido())

def hola2():
    return "Hola!"
# podemos tomar una funcion como parametro
def test(funcion):
    print(funcion())
# y luego pasar la funcion como argumento
test(hola2)