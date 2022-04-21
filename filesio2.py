from io import open

fichero = open("fichero.txt", "r")
fichero.seek(10)
texto = fichero.read()
fichero.close()
print(texto)