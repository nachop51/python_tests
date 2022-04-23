# funciones generadoras

def pares(n):
    for numero in range(n + 1):
        if numero % 2 == 0:
            yield numero

print(pares(10))
for numero in pares(10):
    print(numero)

print([numero for numero in pares(10)])

pares = pares(3)
print(next(pares))
print(next(pares))

l = [1,2,3,4,5]
l = iter(l)
print(l)
print(next(l))
print(next(l))
print(next(l))

s = "Hola"
s = iter(s)
print(s)
print(next(s))
print(next(s))
print(next(s))

# Completa el ejercicio
# Completa el ejercicio
def cuadrados(numero):
    for i in range(1, numero+1):
        yield (i, i**2)

print(list(cuadrados(5)))