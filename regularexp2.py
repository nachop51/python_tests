import re

texto = "hla hola hoola hooola hoooooola"
# print(re.findall('hla', texto))
# print(re.findall('hola', texto))

def buscar(patrones, texto):
    for patron in patrones:
        print(re.findall(patron, texto))

patrones = ['hla', 'hola', 'hoola']
buscar(patrones, texto)

texto = "hla hola hoola hooola hoooooola"

# el * cuenta como 0 o mas veces, esto sirve para buscar 
# ho* sin la 0 o con todas las o a la derecha
patrones = ['ho', 'ho*']
buscar(patrones, texto)

# encuentra todas las palabras del texto
patrones = ['ho', 'ho*la']
buscar(patrones, texto)
# encuentra solo cuando es hla
patrones = ['ho', 'hu*la']
buscar(patrones, texto)
# el + cuenta solo si la letra esta 1 o mas veces
patrones = ['ho*', 'ho+']
buscar(patrones, texto)

# el ? sirve para buscar si esta 0 o 1 vez
# solo devuelve hasta la primera 0, si no tiene devuelve el primer caracter
patrones = ['ho*', 'ho+', 'ho?']
buscar(patrones, texto)

# busca la ho si no esta la cuenta, y si esta 1 sola vez tambien, los demas casos no
patrones = ['ho*', 'ho+', 'ho?la']
buscar(patrones, texto)

# esto indica la cantidad de veces que se tiene que repetir el caracter anterior
# sintaxis rango {n}
patrones = ['ho{0}la', 'ho{1}la', 'ho{3}la']
buscar(patrones, texto)
# tambien podemos especificar un rango de veces que se repita la letra de esta manera
# sintaxis rango {n, m}
patrones = ['ho{0,1}la', 'ho{1,2}la', 'ho{2,10}la']
buscar(patrones, texto)