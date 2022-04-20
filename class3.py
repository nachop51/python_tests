class Pelicula:
    # constructor de la clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se creo la pelicula", self.titulo)
    # destructor de clase
    def __del__(self):
        print("Se borro la pelicula", self.titulo)
    # modifica la funcion str
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo,self.lanzamiento, self.duracion)
    def __len__(self):
        return self.duracion

class Catalogo:
    peliculas = []
    def __init__(self, peliculas=[]):
        self.peliculas = peliculas
    
    def agregar(self, p):
        self.peliculas.append(p)
    def mostrar(self):
        for p in self.peliculas:
            print(p)
    def borrar(self, p):
        del(p)


p = Pelicula("El Padrino", 175, 1972)
# print(str(p))
# print(len(p))
c = Catalogo([p])
c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))
c.mostrar()