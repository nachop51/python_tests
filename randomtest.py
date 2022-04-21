import random

# random() genera numeros aleatorios entre 0 y 1, sin incluir el 1
r = random.random()
print(r)

# uniform(x, y) genera numeros aleatorios entre x e y sin incluir y
r = random.uniform(0.5, 5.3)
print(r)

# de la misma forma que uniform pero con numeros enteros
r = random.randrange(0, 20)
print(r)
# tambien puede tomar un tercer parametro el cual le indicaria
# que solo muestre numeros multiplos de n, ejemplo
r = random.randrange(0, 101, 2)
print(r)

# tambien se pueden elegir chars aleatorios de un string
s = "Hola mundo!"
print(random.choice(s))

# tambien sirve para listas
l = [1,2,3,4,5]
print(random.choice(l))

# entrevera los items de una lista y la modifica
random.shuffle(l)
print(l)

# elige x elementos aleatorios de una lista
print(random.sample(l, 2))