# todas son expresiones iguales
# las funciones lambda son funciones anonimas que lo que intentan
# es simplificar lo maximo posible una funcion, de esta forma
def doblar(num):
    resultado = num * 2
    return (resultado)
print(doblar(5))

def doblar2(num):
    return num * 2
print(doblar2(5))

def doblar3(num): return num * 2
print(doblar3(5))

doblar4 = lambda num: num * 2
print(doblar4(2))

impar = lambda x: x % 2 != 0
print(impar(5))

revertir = lambda string: string[::-1]
print(revertir("Hola"))

sumar = lambda x, y: x + y
print(sumar(24,5))
