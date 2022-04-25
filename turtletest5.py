import turtle as t

t.setup(500,500)

t.shape("turtle") 
t.color("green")

# Creamos funciones para cada acción
def derecha():
    t.seth(0)
    t.forward(20)
    
def izquierda():
    t.seth(180)
    t.forward(20)
    
def arriba():
    t.seth(90)
    t.forward(20)
    
def abajo():
    t.seth(270)
    t.forward(20)
    
def salir():
    t.bye()

# Enlazamos cada función a una tecla
t.onkey(arriba, "w")
t.onkey(izquierda, "a")
t.onkey(derecha, "d")
t.onkey(abajo, "s")
t.onkey(salir, "e")
    
# Hacemos que tortuga esté atenta al teclado
t.listen()

t.done()
t.bye()