a = 10
b = a
a = 1000
print(a, b)

lista1 = [1,2,3,4,5]
# esto lo que hace es crear una copia de la referencia en la memoria
# de la lista1, como un puntero a la lista1 pero con otro nombre
lista2 = lista1
lista1[0] = 1000
print(lista2)

def memoria(obj):
    print(f"{hex(id(obj))}")

memoria(lista1)
memoria(lista2)
memoria(a)
memoria(b)