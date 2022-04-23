# filter es una funcion anonima que devuelve una objeto iterable

numeros = [2, 5, 10, 23, 50, 33]

def multiple(n):
    if n % 5 == 0:
        return True

l = filter(multiple, numeros)
print(l)
print(next(l))
print(next(l))
print(next(l))

# la ventaja de las funciones lambda es que se crean a momento de ejecucion
# esta es una forma de usar la funcion filter y lambda al mismo tiempo
print(list(filter(lambda n: n%5==0, numeros)))

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

menores = filter(lambda persona: persona.edad < 18, personas)
for menor in menores:
    print(menor)