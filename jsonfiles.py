from io import open
import json

contactos = [
    ("Manuel", "Desarrollador Web", "manuelejemplo.com"),
    ("Lorena", "Gestora de proyectos", "1lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javiereejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

datos = []
# datos = {"contactos" : []}

for nombre, trabajo, email in contactos:
    datos.append({"nombre": nombre, "trabajo": trabajo, "email": email})
print(datos)

with open("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)

datos = None

with open("contactos.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"], contacto["trabajo"], contacto["email"])

# de esta forma estamos guardando diccionarios simples dentro de una lista, en formato Json
# pero tambien esta la posibilidad de guardarlo como un diccionario

datos = {"contactos" : []}

for nombre, trabajo, email in contactos:
    datos["contactos"].append({"nombre": nombre, "trabajo": trabajo, "email": email})

with open("contactos2.json", "w") as jsonfile:
    json.dump(datos, jsonfile)

datos = None

with open("contactos2.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos["contactos"]:
        print(contacto["nombre"], contacto["trabajo"], contacto["email"])

# de esta forma estamos guardando un diccionario con una lista de diccionarios dentro