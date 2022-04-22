# operadores encadenados
print(1 < 2 and 2 < 3)
# estas son dos formas de expersar lo mismo
print(1 < 2 < 3)

num = 35

if num >= 0 and num <= 100:
    print("El número {} se encuentra entre 0 y 100". format(num))
else:
    print("El número {} no se encuentra entre 0 y 100".format(num))

# estas expresiones tambien son iguales

if 0 <= num <= 100:
    print("El número {} se encuentra entre 0 y 100". format(num))
else:
    print("El número {} no se encuentra entre 0 y 100".format(num))
