import turtle as t

t.setup(500, 500) # configurar el espacio de trabajo

t.shape("turtle") # generamos la tortuga
t.color("green")  # le damos color a la tortuga

def rectangulo(px, py, ancho, alto):
    t.penup()
    t.goto(px + ancho / 2, py + alto / 2)
    t.seth(180)
    t.pendown()
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(alto)

rectangulo(0, 0, 400, 300)
rectangulo(0, 0, 300, 200)
rectangulo(0, 0, 200, 100)
rectangulo(0, 0, 50, 50)

t.done() # Done y bye cierran todas las rutinas
t.bye()  # y cortan la ejecucion de turtle