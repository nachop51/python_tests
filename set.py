c = set()
c.add(1)
c.add(2)
c.add(3)
# forma de añadir elementos a un conjunto
print(c)
c.discard(1)
# forma de descartar elementos de un conjunto
print(c)
c.add(1)
print(c)
c2 = c
c2.add(4)
print(c,c2)
c.discard(4)
print(c,c2)
# al intentar crear una copia de forma normal, no estamos creando otra copia
# si no otra referencia al mismo conjunto, los conjuntos tienen su propio metodo
# para copiar su contenido y es .copy()
c2 = c.copy()
print(c2, "copia de c")
c.add(4)
print(c,"original",c2,"copia")
c.clear()
c2.clear()
# clear borra todo el contenido
print(c,c2)

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
# isdisjoint devuelve true si los conjuntos no tienen valores en comun
print(c1.isdisjoint(c3))
print(c1.isdisjoint(c2))
# issubset devuelve si c1 es un subconjunto de c2
print(c1.issubset(c4))
print(c3.issubset(c4))
# devuelve si es un superconjunto de c1, es decir, si lo contiene
print(c4.issuperset(c1))
# union une los dos conjuntos
print(c1.union(c2))
print(c1.union(c2) == c4)
# update es como union, pero si modifca el conjunto
c1.update(c2)
print(c1)

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}
# devuelve la diferencia de conjuntos
print(c1.difference(c2))
# actualiza el conjunto a la diferencia de los mismos
print(c1.difference_update(c2))
c1 = {1,2,3}
# devuelve un conjunto donde coinciden los valores
print(c1.intersection(c2))
# al igual que con difference pero con intersection
print(c1.intersection_update(c2))
# symmetric_difference devuelve un conjunto con todo lo que no coincide entre los conjuntos
c1.symmetric_difference(c2)
