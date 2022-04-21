import datetime

# modulo para importar fechas
dt = datetime.datetime.now()
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

# los objetos dt en realidad son tuplas, por lo tanto son inmutables

print(f"Hora actual: {dt.hour}:{dt.minute}:{dt.second}")
# print("Hora actual: {}:{}:{}".format(dt.hour, dt.minute, dt.second))
# print("Hora actual: %d:%d:%d" % (dt.hour,dt.minute,dt.second))
# solo son tres formas de hacer lo mismo
print(f"Fecha actual: {dt.day}/{dt.month}/{dt.year}")

# forma de crear una fecha:
dt = datetime.datetime(2001, 12, 15)
print(dt)
# si quisieramos modificar esta fecha, no podriamos hacerlo
# de la forma normal, ya que es una tupla, pero datetime tiene un metodo
# para modificar las fechas, el cual es replace
dt = dt.replace(year=2002)
print(dt)

dt = datetime.datetime.now()
print(dt.isoformat()) # formateo de fecha y hora general, el mas usado

print(dt.strftime("%A %d %B %Y %I:%M"))
# %I se usa para formato 12 horas
# %H se usa para formato 24 horas

# como nota, por defecto sale en ingles, pero podriamos importar el modulo
# locale que lo que haces es decirle a python el lenguaje que queremos utilizar
# para importarlo se usa:
# import locale
# y para setear el lenguaje se tiene que tener en cuenta el codigo del lenguaje
# locale.setlocale(locale.LC_ALL, "es-uy")
# esto se tiene que ejecutar antes del datatime obviamente
