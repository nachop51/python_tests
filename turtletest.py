import turtle as t

t.setup(500, 500) # configurar el espacio de trabajo

t.shape("turtle") # generamos la tortuga
t.color("green")  # le damos color a la tortuga

print(t.pos())
t.forward(250) # se desplaza 250 px
t.left(90)     # gira 90°
t.forward(250) # se desplaza 250 px
t.left(90)     # gira 90°
t.forward(500) # se desplaza 500 px
t.left(90)     # gira 90°
t.forward(500) # se desplaza 500 px
t.left(90)     # gira 90°
t.forward(500) # se desplaza 500 px
t.left(90)     # gira 90°
t.forward(250) # se desplaza 250 px

print(t.pos())

t.done() # Done y bye cierran todas las rutinas
t.bye()  # y cortan la ejecucion de turtle