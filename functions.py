def resta(a=None, b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    else:
        return a-b
print(resta(12, 40))
print(resta(a=10, b=5))
print(resta(b=10, a=5))

def doblar_valores (numeros):
    for i,n in enumerate(numeros):
        numeros [i] *= 2
ns = [10,50,100]
# no varia el valor de la lista porque es una copia
doblar_valores (ns[:])
print(ns)
# el valor de la lista cambia porque se le pasa un puntero a la lista
doblar_valores (ns)
print(ns)

# funciones variadicas
def indeterminados(*args):
    # print(args)
    for arg in args:
        print(arg)

indeterminados(12340, "asdñkj", [1,2,3])

# diccionario
def indet(**kwargs):
    # print(kwargs)
    # for kwarg in kwargs.items(): otra forma de printear valores
    #     print(kwarg)             de un diccionario
    # for k in kwargs.keys():      para printear las claves
    #     print(k)                 de un diccionario
    for k, v in enumerate(kwargs):
        print(k,"", kwargs[v])

indet(n=10,c="hola",l=[1,2,3,4,5,6,7,8,9])

# funcion variadica y con diccionario
def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t+=arg
    print("Sumatorio indeterinado es", t)
    for kwarg in kwargs:
        print (kwarg," ", kwargs[kwarg])
super_funcion(10,50,-1,1.56,1042,-324, nombre="Hector", edad=27)