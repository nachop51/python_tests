import turtle as t

t.setup(500, 500) # configurar el espacio de trabajo

t.shape("turtle") # generamos la tortuga
t.color("green")  # le damos color a la tortuga

def poligono_regular(px, py, radio, lados):
    t.penup()
    t.goto(px, py - radio)
    t.circle(radio)
    
    angulo = 360 / lados
    vertices = []
    for i in range(lados):
        t.penup()
        t.goto(px, py)
        t.seth(angulo * i + 1)
        t.forward(radio)
        vertices.append(t.pos())
    t.goto(vertices[0])
    t.pendown()
    for v in vertices:
        t.goto(v)
    t.goto(vertices[0])

t.speed(200)
for n in range(3, 21):
    poligono_regular(0, 0, n*10, n)

t.done() # Done y bye cierran todas las rutinas
t.bye()  # y cortan la ejecucion de turtle