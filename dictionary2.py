colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
# print(colores["amarillo"]) # de esta forma se puede acceder al valor del diccionario
# otra forma de obtener los valores de un diccionario
print(colores.get("amarillo", "no se encuentra"))
print(colores.get("negro", "no se encuentra"))
# forma rapida de ver si un valor esta en el diccionario
print('negro' in colores)
print('blue' in colores)

# devuelve una lista con las claves
print(colores.keys())
# devuelve una lista con los valores
print(colores.values())
# devuelve una lista con los valores y las claves
print(colores.items())

# forma normal de recorrer el diccionario
# for c in colores:
#     print(colores[c])

# obtener las claves
for c in colores.keys():
    print(c)
# obtener los valores
for c in colores.values():
    print(c)
# obtener claves y valores
for c, v in colores.items():
    print(c, v)

# los diccionarios tambien tienen el metodo pop
print(colores.pop("amarillo", "no se ha encontrado"))
print(colores.pop("violeta", "no se ha encontrado"))
print(colores)

# clear vacia el diccionario
colores.clear()
print(colores)