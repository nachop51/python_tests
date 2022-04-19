# print("Hello".upper()) # mayuscula
# print("Hello".lower()) # minuscula
# print("Hello".capitalize()) # inicial con mayuscula
# print("Hello".title()) # todas las iniciales con mayuscula
# print("Hello".count("l")) # cuenta la cantidad de veces que aparace una cadena dada
# print("Hello".find("lo")) # devuelve el indice en el que aparce la cadena dada
# print("Hello".rfind("l")) # encuentra la ultima coincidencia con la cadena dada

c = "100"
print(c.isdigit()) # is digit de la shell(nacho)
c2 = "ABC123asd?"
print(c2.isalnum()) # comprueba si el string contiene solo numeros y letras
c3 = "ASDb2"
print(c3.isalpha()) # comprueba si solo contiene letras
c4 = "asdasd"
print(c4.islower()) # comprueba si solo tiene letras minusculas
c5 = "ASDSAD"
print(c5.isupper()) # comprueba si solo tiene letras mayusculas
c6 = "Hola mundo"
print(c6.istitle()) # comprueba si es tipo title
c7 = "    "
print(c7.isspace()) # comprueba si solo contiene espacios
c8 = "Hola mundo"
print(c8.startswith("Hola")) # comprueba si una cadena empieza con otra cadena dada
c9 = "Hola mundo"
print(c9.startswith("mundos")) # comprueba si una cadena termina con otra cadena dada
c10 = "Hola  mundo mundo"
print(c10.split()) # split funciona como strtok pero solo con espacios si no se le pone nada
print(c10.split("o")) # ahora tokeniza por o
c11 = " "
print(c11.join("holamundo")) # join concatena cada letra del string con el string dado
c12 = "    Hola  mundo    "
print(c12.strip()) # como strtok pero solo al principio y al final, tambien funciona con " " por defecto
c13 = "Hola mundo mundo"
print(c13.replace("o", "0")) # cambia el primer parametro por el segundo el tercer parametro
print(c13.replace(" mundo", "", 1)) # sirve para indicar la cantidad de veces a sustituir