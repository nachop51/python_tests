# def hola():
#     print("Hola!")

# def adios():
#     print("Adios!")

def monitorizar(func):
    def decorar():
        # func.__name__ devuelve el nombre de la funcion
        print("\tSe está a punto de ejecutar la funcion:", func.__name__)
        func()
        print("\tSe ejecutó la funcion:", func.__name__)
    return decorar

# monitorizar(hola)()
# hay que volver a ejecutar la funcion, porque el return de llamar a monitorizar
# devuelve otra funcion en el return
# monitorizar(adios)()

# sirve como funcion decorativa
# su objetivo es complementar la ejecucion de la funcion
@monitorizar
def hola():
    print("Hola!")

@monitorizar
def adios():
    print("Adios!")

hola()
adios()

# el problema es que hay que adaptar estas funciones para que tomen parametros
# y la sintaxis es facil, con args y kwargs
def monitorizar_args(func):
    def decorar_args(*args, **kwargs):
        # func.__name__ devuelve el nombre de la funcion
        print("\tSe está a punto de ejecutar la funcion:", func.__name__)
        func(*args, **kwargs)
        print("\tSe ejecutó la funcion:", func.__name__)
    return decorar_args

@monitorizar_args
def hola2(nombre):
    print(f"Hola {nombre}!")

@monitorizar_args
def adios2(nombre):
    print(f"Adios {nombre}!")

hola2("Nacho")
adios2("Nacho")
