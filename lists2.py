lista = [1,2,3,4]
lista.append(5) # agrega un nuevo item al final
print(lista)

lista.clear() # vacia una lista
print(lista)

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2) # concatena dos listas
print(l1)

lista = [1,1,4,2]
print(lista.count(1)) # cuenta la cantidad de apariciones
print(lista.index(2)) # busca la primera coincidencia en la lista
print(lista)
lista.insert(0, 0) # lo primero es el index, y lo segundo es a insertar
print(lista)
l = [5,10,15,25]
print(l)
l.insert(-1, 20) # inserta en la penultima posicion
print(l)
l.insert(5, 30)
print(l)
l.insert(234, 300) # si el index pasado supera la ultima posicion, solo se pone al final
print(l)

# pop devuelve el resultado que se saco
l.pop() # saca el ultimo elemento de una lista
print(l)
l.pop(0) # saca el elemento por index de una lista
print(l)
l.remove(20) # saca por referencia
print(l)

l.reverse() # da vuelta la lista
print(l)

# truco lamentruco para dar vuelta un string usando listas
cadena = "Hola mundo"
print(cadena)
lista = list(cadena)
print(lista)
lista.reverse()
print(lista)
cadena = "".join(lista)
print(cadena)

lista = [5, -10, 34, 0, -231, 492]
print(lista)
lista.sort() # ordena la lista por tamaño
print(lista)
lista.sort(reverse=True) # ordena la lista por tamaño inverso
print(lista)