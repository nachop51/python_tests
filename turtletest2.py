import turtle as t

t.setup(500, 500) # configurar el espacio de trabajo

t.shape("turtle") # generamos la tortuga
t.color("green")  # le damos color a la tortuga

t.penup()   # penup levanta el lapiz para que la tortuga no dibuje
t.forward(200)
t.left(90)
t.pendown() # pendown baja el lapiz
t.forward(150)
t.left(90)
t.forward(400)
t.left(90)
t.forward(300)
t.left(90)
t.forward(400)
t.left(90)
t.forward(150)

t.done() # Done y bye cierran todas las rutinas
t.bye()  # y cortan la ejecucion de turtle