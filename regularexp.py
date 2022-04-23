import re

texto = "En esta cadena se encuentra una palabra magica"

def buscar(s, texto):
    # si re no encuentra nada deuvelve None, o null
    r = re.search(s, texto)
    if r is not None:
        print("Se ha encontrado la palabra")
        # return (r.start(), r.end())
        # en vez de usar esta tupla tambien se puede usar r.span()
        # y por ultimo r.string() que devuelve el texto entero (la variable texto)
        return r.span()
    else:
        print("No se ha encontrado la palabra")

r = buscar("magica", texto)
print(r[0], r[1])
r = buscar("hola", texto)
if r is not None:
    print(r[0], r[1])

texto = "Hola mundo"
# match devuelve un objeto diciendo si se encontro coincidencia
a = re.match("Hola", texto)
print(a)
# en caso de no encontrar deuvelve None
a = re.match("hola", texto)
print(a)

texto = "Vamos a dividir esta cadena"
# re.split funciona como split
l = re.split(' ', texto)
print(l)

texto = "Hola amigo"
# re.sub cambia el s1, por el s2
s = re.sub("amigo", "amiga", texto)
print(s)

texto = "hola adios hola hola"
# finall devuelve todas las coincidencias 
l = re.findall("hola", texto)
print(l)

texto = "hola adios hello bye"
# tambien podemos buscar las coincidencias de dos palabras distintas usando un pipeline
l = re.findall("hola|hello", texto)
print(l)
