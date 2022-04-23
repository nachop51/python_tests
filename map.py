numeros = [2, 5, 10, 23, 50, 33]

def doblar(n):
    return n*2
# map aplica la misma funcion a todos los elementos de una lista
n = map(doblar, numeros)
# map devuelve un objeto iterable
print(list(map(doblar, numeros)))
print(next(n))
print(next(n))
print(next(n))
# al avanzar con next se avanza el puntero y no muestra lo anterior
print(list(n))

print(list(map(lambda x: x*2, numeros)))

a = [1,2,3,4,5]
b = [6,7,8,9,10]
# len(a) == len(b) si no no es posible
print(list(map(lambda x,y: x*y, a, b)))
c = [11,12,13,14,15]
print(list(map(lambda x,y,z: x*y*z, a, b, c)))



# forma normal de hacerlo #
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre} de {self.edad} años"

personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manual", 78),
    Persona("Eduardo", 12)
]

def incrementar(persona):
    persona.edad += 1
    return persona
personas = map(incrementar, personas)
for persona in personas:
    print(persona)

########################################

# con map y lambda
personas = [
    Persona("Juan", 35),
    Persona("Marta", 16),
    Persona("Manual", 78),
    Persona("Eduardo", 12)
]

personas = map(lambda persona: Persona(persona.nombre, persona.edad+1), personas)
for persona in personas:
    print(persona)

# Funciones anónimas
# Utilizando dos funciones anónimas anidadas en una sola línea, debes:
# 1. Mapear una lista llamada numeros de la cuál no conoces su contenido y dividir sus
# valores entre 2.
# 2. A su vez debes filtrar el resultado de esa lista mapeada y eliminar los números que no
# sean múltiples de 5.
# El resultado final será una lista cuyos números son la mitad de los originales y sólo quedarán los que sean múltiples de 5.

numeros = list(filter(lambda x: x%5==0, map(lambda x: x/2, numeros)))
print(numeros)