<<<<<<< HEAD
from collections import Counter
=======
from collections import Counter, defaultdict, namedtuple
from typing import OrderedDict
>>>>>>> e2f97f1f936871c4e22e6772ca2541713d05c589

l = [1,2,3,4,1,2,3,1,2,1]
print(Counter(l))

p = "palabra"
print(Counter(p))

animales = "gato perro canario perro canario perro"
print(Counter(animales))

# contador "perfecto"
c = Counter(animales.split())
print(c)
# muestra el mas repetido
print(c.most_common(1)) # el que mas se repite
print(c.most_common(2)) # los dos que mas se repiten
print(c.most_common())  # todos por orden

l = [10, 20, 30, 40, 10, 20, 30, 10, 20, 10]
c = Counter(l)
print(c)

print(c.items())
# valores de la lista
print(c.keys())
# numero de repeticiones
print(c.values())
# contador como len()
sum(c.values())
<<<<<<< HEAD
=======

# Para que los diccionarios no den error cuando se intenta
# acceder a una clave que no es valida, podemos importar el modulo
# defaultdict, que nos permite poner un valor por defecto para que no
# corte el programa, ejemplo:
d = defaultdict(float)
# diccionario vacio
# al intentar acceder a una clave vacia no corta la ejecucion del programa
# si no que devuelve un valor por defecto el cual es 0.0
print(d['10'])
# ahora si consultamos el diccionario se creo la clave '10':'0'
print(d)
# tambien se pueden crear defaultdicts de str
d = defaultdict(str)
# clave no existente
print(d['asd'],"<-- clave vacia, al haber sido declarado string")
print(d)
# tambien se pueden declarar diccionarios de la clase object
# o de la clase int como en el siguiente ejemplo
d = defaultdict(int)
d["key"] = 10.5
# el hecho de haber declarado la clave default como int no afecta
# al contenido de las variables del diccionario, solo a la clave default
print(d["key"], d["nonexistent"])
print(d)

n = OrderedDict()
n["uno"] = "one"
n["dos"] = "two"
n["tres"] = "three"
print(n)

# como los diccionarios son desordenados por defecto
# al intentar comparar dos diccionarios armados al reves
# en realidad tienen los mismos objetos, por lo tanto son iguales
n1 = {}
n1["uno"] = "one"
n1["dos"] = "two"

n2 = {}
n2["dos"] = "two"
n2["uno"] = "one"

print(n1 == n2)

# pero al hacer lo mismo con diccionarios ordenados
# en realidad no nos estamos refiriendo al mismo objeto
# ya que aca si importa el orden de creacion para el objeto
n1 = OrderedDict()
n1["uno"] = "one"
n1["dos"] = "two"

n2 = OrderedDict()
n2["dos"] = "two"
n2["uno"] = "one"

print(n1 == n2)

# tuplas con nombre
# tuplas: lista ordenada, en la que se pueden repetir objetos pero es
# inmutable, tambien nos podemos referir a sus objetos por indices

# una tupla con nombre es una especie de clase pero mas simple
# se comporta como tupla y como clase, como se puede ver abajo
Persona = namedtuple('Persona', 'nombre apellido edad')
p = Persona(nombre="Nacho", apellido="Peralta", edad=19)
print(p.nombre)
print(p.apellido)
print(p.edad)
print(p)
print(type(p))
print(p[0])
print(p[1])
print(p[2])
>>>>>>> e2f97f1f936871c4e22e6772ca2541713d05c589
