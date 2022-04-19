# Modulo
def func():
    print("Hola!")

class Clase:
    def __init__(self):
        print("Se creo una instacia de Clase")

# esta comprobacion sirve para que no se ejecute el codigo si el nombre
# del archivo que la ejecuta, no es __main__, el archivo principal es el que se llama asi
if __name__ == "__main__":
    func()
    Clase()
