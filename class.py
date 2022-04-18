# la clase es necesaria para crear objetos
class Galleta:
    chocolate = False

galleta = Galleta()
galleta2 = Galleta()

# Descomentando esto se puede ver de que tipo es cada valor introducido
# def Hola():
#     pass
# 
# print(type(galleta))
# print(type(10))
# print(type("asd"))
# print(type([1,2,3]))
# print(type({}))
# print(type(Hola))
# print(type(()))
# print(type(set()))
# print(type(True))
# print(type(32.42))

galleta.color = "Negra"
galleta.size = 5
galleta.chocolate = True
print("La galleta es",galleta.color)
print(galleta.size)
print(galleta.chocolate)
galleta2.color = "Marron"
galleta2.size = 4
print("La galleta es",galleta.color)
print(galleta2.size)
print(galleta2.chocolate)