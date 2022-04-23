import re

def buscar(patrones, texto):
    for pat in patrones:
        print(re.findall(pat, texto))

texto = "hala hela hila hola hula"
# de esta forma podemos buscar una letra en conjunto de letras en especial
# por ejemplo aca estariamos buscando las palabras hola y hula por separado
# al indicarle h[ou]la se refiere a que la o y la u ambas sirven por separado
patrones = ["h[ou]la", "h[aio]la", "h[aeiou]la"]
buscar(patrones, texto)

texto = "haala heeela hiiiiila hoooooola huuuuuuuula"
# tambien podemos combinar expresiones regulares de esta forma
# indicandole que queremos encontrar la a o la e, de forma indepentiente
# * n o mas veces, o en el segundo caso, la i o la o, de 3 a 9 veces
patrones = ["h[ae]la", "h[ae]*la", "h[io]{3,9}la"]
buscar(patrones, texto)

texto = "hala hela hila hola hula"
# luego esta el caso contrario, donde podemos usar el caracter
# de exclusion, para buscar todos los casos menos el cual indicamos
# los dos ejemplos siguientes son contrarios
patrones = ["h[o]la", "h[^o]la"]
buscar(patrones, texto)

texto = "hola hela Hola eola gela Dela sdjh sdzd U377 Ysdj"
# de esta manera podemos indicar rangos para buscar
# y combinando expersiones, buscar 4 caracteres random,
# o un caracter en un rango especial y otros caracteres
patrones = ['h[a-z]la', 'h[0-9]la', '[A-z]{4}', "[A-Z][A-z0-9]{3}"]
buscar(patrones, texto)

texto = "Esto es un texto random 23 y un numero random 2408"
# esto es un quilombo de explicar, mejor dejo las referencias
# nota: el mas sirve para buscar patrones que se repitan 1 o mas veces
# ref1: \d numérico
#       \D no numérico
#       \s espacio en blanco
#       \S no espacio en blanco
#       \w alfanumérico
#       \W no alfanumérico
# ref2: El problema que encontraremos 
#       en Python a la hora de definir código escapado, 
#       es que las cadenas no tienen en cuenta el \ a 
#       no ser que especifiquemos que son cadenas en 
#       crudo (raw), por lo que tendremos que precedir 
#       las expresiones regulares con una 'r'.
patrones = [r"\d", r"\d+", r"\D", r"\D+", r'\s', r"\S", r"\S+", r"\w", r"\w+", r"\W", r"\W+"]
buscar(patrones, texto)