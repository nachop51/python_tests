import sqlite3

# de esta manera nos conectamos a la base de datos
# y si no existe dicha base la crea
conex = sqlite3.connect("db.db")
# lo primero y esencial es crear un cursor, de esta forma
# asi podemos crear consultas a la base de datos
cursor = conex.cursor()
# esto vendria a ser la creacion del query, la peticion a la base de datos
# descomentando esto de abajo, lo que hacemos es crear la base de datos, y la sintaxis es facil
# cursor.execute(SQL_QUERY) donde SQL_QUERY es la peticion en el lenguaje SQL
# lo que hace este codigo es crear una tabla, con nombre, edad y un email
# cursor.execute("CREATE TABLE users (name VARCHAR(100), age INTEGER, email VARCHAR(100))")
#
# al igual que antes esta es otra peticion, pero lo que hacemos aca es insertar
# un nuevo dato a la tabla, en este caso le pasamos los valores que antes pedimos 
# cursor.execute("INSERT INTO users VALUES ('Nacho', 19, 'nachoperalta0@gmail.com')")
# 
# y esta ultima query es para obtener lo que insertamos dentro de la tabla
# esto asgina un objeto a cursor, el cual con un metodo lo podemos convertir en una tupla
# cursor.execute("SELECT * FROM users")
# con cursor.fetchone()
# user = cursor.fetchone()
# ahora si podemos mostrarlo
# print(user)
#
# tambien podemos insertar de forma "masiva" a la base de datos
# con una lista y tuplas con los datos
# users = [
#     ('Mario', 51, 'mario@gmail.com'),
#     ('Mercedes', 38, 'mercedes@gmail.com'),
#     ('Juan', 19, 'juan@gmail.com'),
# ]
# entonces, en vez de usar execute, usamos execute many, y la sintaxis es la siguiente
# VALUE (?,?,?), users <- la lista de tuplas con los datos
# cursor.executemany("INSERT INTO users VALUES (?,?,?)", users)
# de esta forma estamos agregando a los tres usuarios a la misma vez
#
# luego para recuperarlos es sencillo, al igual que antes traemos todos
# cursor.execute("SELECT * FROM users")
# 
# pero ahora en vez de hacer fetchone, hacemos fetchall
# users = cursor.fetchall()
# y despues podemos solo mostrar los usuarios, o acceder a sus indices con users[0]
# o directamente mostrar todos sus datos de esta forma
# for user in users:
    # print(user)

# y por ultimo e importante, por medidas de seguridad, tenemos que confirmar los cambios
# para que estos hagan efecto en la basde de datos, como una especie de git commit, antes de subir los cambios
conex.commit()

conex.close()
# cerrar la conexion