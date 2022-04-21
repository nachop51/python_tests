from io import open

# open se usa para abrir un archivo de una forma especifica
# lo primero que toma es el nombre y lo segundo es la forma
# en que se va a abrir el archivo
texto = "Texto\nOtra linea"
# w es modo escritura
# al abrir un archivo en modo escritura borra todo el contenido anterior
fichero = open("fichero.txt","w")
# con el metodo write escribimos adentro del archivo
fichero.write(texto)
# y por ultimo cerrarlo
fichero.close()

# r es modo lectura
# de no existir el archivo daria error
fichero2 = open("fichero2.txt", "r")
# al abrir en modo lectura, no pasa nada
texto = fichero2.read()
fichero2.close()
print(texto)

fichero = open("fichero2.txt", "r")
# de esta forma guardamos todas las lineas en una lista
lineas = fichero.readlines()
fichero.close()
print(lineas)

# a es modo append, el modo append si no existe el archivo lo crea
# fichero = open("fichero2.txt", "a")
# fichero.write("\nCuarta linea")
# fichero.close()

# si repetimos readline vamos avanzando linea a linea
# fichero = open("fichero2.txt", "r")
# texto = fichero.readline()
# texto = fichero.readline()
# fichero.close()
# print(texto)

# forma de recorrer un archivo y mostrar su contenido
with open("fichero2.txt", "r") as fichero:
    for linea in fichero:
        print(linea, end="")