from io import open
import csv

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javierejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

# al abrir un fichero con with no hace falta cerrarlo manualmente
with open("contactos.csv", "w", newline="\n") as csvfile:
    # tenemos que hacer un escritor, asi de esta forma podemos guardar los datos en el archivo csv
    writer = csv.writer(csvfile, delimiter=",")
    for contacto in contactos:
        # writerow es una funcion que nos sirve para escribir por filas
        writer.writerow(contacto)

with open("contactos.csv", newline="\n") as csvfile:
    # ahora tenemos que crear un lector de datos para asi poder extraer la informacion
    reader = csv.reader(csvfile, delimiter=",")
    # ahora el readear leyo todos los datos que le habiamos guardado antes
    # y los conserva en forma de listas que podemos recorrer de esta manera 
    # for contacto in reader:
    #     print(contacto)
    # pero tambien podemos recuperar manualmente cada campo, de esta forma
    # usando una especie de asignacion multiple
    for nombre, trabajo, email in reader:
        print(nombre, trabajo, email)

# csv files pero con diccionarios
with open("contactosDict.csv", "w", newline="\n") as csvfile:
    # lo primero es crear las casillas que especifiquen que es cada cosa
    campos = ["nombre", "trabajo", "email"]
    # entonces despues con fieldnames les pasamos el nombre de las casillas
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    # con la funcion DictWriter creamos nuestro escritor de diccionarios
    writer.writeheader()
    # y con la funcion writeheader escribimos los nombres de las casillas
    for nombre, trabajo, email in contactos:
        # recorremos la lista de contactos refiriendonos a cada casilla
        writer.writerow({
            # y asignamos a cada campo un valor de esta forma
            "nombre": nombre, "trabajo": trabajo, "email": email
        })

# para leer es lo mismo que con listas, pero difiere en la forma de obtener los datos
with open("contactosDict.csv", newline="\n") as csvfile:
    # necesitamos un reader de diccionarios
    reader = csv.DictReader(csvfile)
    # DictReader se encarga automaticamente de la delimitacion y nos guarda el diccionario
    for contacto in reader:
        # y despues para leer los datos solo hace falta referirnos a las claves
        print(contacto["nombre"], contacto["trabajo"], contacto["email"])