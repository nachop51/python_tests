from io import open
import pickle

class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)
class Catalogo:
    peliculas = []
    # Constructor de clase
    def __init__(self):
        self.cargar()
    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()
    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catalogo está vacío")
            return
        for p in self.peliculas:
            print(p)
    def cargar(self):
        # el modo ab+ es append binario con funciones de lecutra
        fichero = open("catalogo.pckl", "ab+")
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero esta vacio")
        finally:
            fichero.close()
            print(f"Se han cargado {len(self.peliculas)} peliculas")
    def guardar(self):
        fichero = open("catalogo.pckl", "wb")
        pickle.dump(self.peliculas, fichero)
        fichero.close()
    
    def __del__(self):
        self.guardar()
        print("Se ha guardado el fichero")

c = Catalogo()
c.mostrar()
c.agregar(Pelicula("El Padrino", 175, 1972))
c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))
c.mostrar()
del(c)
c = Catalogo()
c.mostrar()
c.agregar(Pelicula("Prueba", 100, 2000))
del(c)
c = Catalogo()
c.mostrar()
del(c)