# forma tradicional de hacerlo

lista = []

for letra in 'casa':
    lista.append(letra)
print(lista)

# con comprension de listas

lista = [letra for letra in 'casa']
print(lista)

# forma tradicional de hacerlo

lista = []
for numero in range(0, 11):
    lista.append(numero ** 2)
print(lista)

# con comprension de listas

lista = [numero**2 for numero in range(0, 11)]
print(lista)

# forma tradicional de hacerlo

lista = []
for numero in range(0, 11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)

# con comprension de listas

lsita = [numero for numero in range(0, 11) if numero % 2 == 0]
print(lista)

# forma tradicional de hacerlo

lista = []
for numero in range(0, 11):
    lista.append(numero ** 2)
print(lista)

pares = []
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

# con comprension de listas

pares = [numero for numero in [num ** 2 for num in range(0, 11)] if numero % 2 == 0]
print(pares)

# Completa el ejercicio en una línea
multiples = [numero for numero in range(0,501) if numero % 2 == 0 and numero % 3 == 0 and numero % 4 == 0 and numero % 8 == 0]
print(multiples)