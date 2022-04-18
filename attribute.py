class Ejemplo:
    __atributo = "Atributo privado"
    
    def __metodo_privado(self):
        print("Metodo privado")
    def atributo_publico(self):
        return self.__atributo
    def metodo_publico(self):
        self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()