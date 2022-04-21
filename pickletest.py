import pickle

l = [1,2,3,4,5]
# la extencion de pckl es de pickle
# el modo wb es de escritura binaria, que es la manera en la que se almacena
# la informacion en esta clase de ficheros
# (si el fichero existe, lo sobreescribe por completo
# y si no existe lo crea)
fichero = open("lista.pckl", "wb")
# dump, plasma lo que le pasemos al fichero
pickle.dump(l, fichero)
fichero.close()

# el modo rb es de lecutra binaria
fichero = open("lista.pckl", "rb")
# load carga lo que tenga el fichero
# tambien mueve el puntero hacia el final del archivo
lista = pickle.load(fichero)
print(lista)
fichero.close()

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return self.nombre

nombres = ["Hector", "Mario", "Marta"]
personas = []
for n in nombres:
    p = Persona(n)
    personas.append(p)
print(personas)

fichero = open("personas.pckl", "wb")
pickle.dump(personas, fichero)
fichero.close()

fichero = open("personas.pckl", "rb")
pers = pickle.load(fichero)
fichero.close()
for p in pers:
    print(p)
