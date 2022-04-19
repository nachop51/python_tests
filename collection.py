from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]
print(Counter(l))

p = "palabra"
print(Counter(p))

animales = "gato perro canario perro canario perro"
print(Counter(animales))

# contador "perfecto"
c = Counter(animales.split())
print(c)
# muestra el mas repetido
print(c.most_common(1)) # el que mas se repite
print(c.most_common(2)) # los dos que mas se repiten
print(c.most_common())  # todos por orden

l = [10, 20, 30, 40, 10, 20, 30, 10, 20, 10]
c = Counter(l)
print(c)

print(c.items())
# valores de la lista
print(c.keys())
# numero de repeticiones
print(c.values())
# contador como len()
sum(c.values())
