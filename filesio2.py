from io import open

fichero = open("fichero.txt", "r")
# seek mueve el puntero de donde estamos leyendo, x caracteres
fichero.seek(10)
texto = fichero.read()
print(texto)
texto = fichero.read()
print(texto, "\nesta linea esta vacia porque el puntero se movio hasta el final, y no tiene que mas leer")
fichero.seek(0)
texto = fichero.read()
print(texto)
fichero.close()

fichero = open("fichero.txt", "r")
# tambien le podemos indicar a read cuanto queremos leer
texto = fichero.read(5)
print(texto)
# read tambien mueve el puntero, es por eso que haciendo otro read
# despues del read(5), leemos desde el caracter 5 hasta el final del fichero
texto = fichero.read()
print(texto)
fichero.close()

fichero = open("fichero.txt", "r")
texto = fichero.read()
# haciendo esto podemos leer la mitad del texto colocando el puntero en la mitad
# y leyendo hasta el final del fichero
fichero.seek((int)(len(texto) / 2))
texto = fichero.read()
print(texto)
fichero.close()

fichero = open("fichero.txt", "r")
# leer desde la segunda linea hasta el final
fichero.seek(len(fichero.readline()))
texto = fichero.read()
print(texto)
fichero.close()

# el modo r+ sirve para abrir en modo lecutra y escritura, va sobreescribiendo el fichero
fichero = open("fichero.txt", "r+")
fichero.write("Esta linea la modifique usando el modo r+\n")
fichero.close()

# tambien se pueden modificar lineas en especifico
fichero = open("fichero.txt", "r+")
# la funcion readlines devuelve una lista con todas las lineas del archivo
l = fichero.readlines()
# esto movio el puntero hacia el final del archivo
l[2] = "Modifique esta linea desde el script\n"
print(l)
# la funcion writelines nos permite pasar una lista con lineas para modificar el fichero
# hay que traer el puntero hacia el inicio de nuevo
fichero.seek(0)
fichero.writelines(l)
fichero.seek(0)
texto = fichero.read()
fichero.close()
print(texto)