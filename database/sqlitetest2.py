import sqlite3

conex = sqlite3.connect("db4.db")
cursor = conex.cursor()

# usando PRIMARY KEY, hacemos que los datos no se puedan repetir
# cursor.execute('''
#     CREATE TABLE users (
#         id VARCHAR(9) PRIMARY KEY,
#         name VARCHAR(100),
#         age INTEGER,
#         email VARCHAR(100)
#     )
# ''')

# users = [
#     ('1234', 'Nacho', 19, 'nacho@gmail.com'),
#     ('1235', 'Mario', 51, 'mario@gmail.com'),
#     ('1236', 'Mercedes', 38, 'mercedes@gmail.com'),
#     ('1237', 'Juan', 19, 'juan@gmail.com')
# ]

# cursor.executemany("INSERT INTO users VALUES (?,?,?,?)", users)
# si hacemos un insert de esta manera
# cursor.execute("INSERT INTO users VALUES ('1237', 'Juan', 19, 'juan@gmail.com')")
# nos daria un error, porque estamos intentando agregar a la base de datos un valor
# que ya existe y que no se puede repetir, es el id

# AUTOINCREMENT hace que el campo se gestione solo y sea autoincremental
# NOT NULL no permite que la entrada sea vacia
# cursor.execute('''
#     CREATE TABLE productos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )
# ''')

# productos = [
#     ('Teclado', 'Logitech', 19.95),
#     ('Pantalla 21"', 'LG', 89.95)
# ]
# y para pasar el campo auto incremental lo unico que tenemos que hacer es que sea null
# de esta forma estamos pasando todos los datos correctamente
# cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)

# unique hace referencia a que esa clave no se puede repetir
# y que tampoco se puede repetir en ningun otro registro
# cursor.execute('''
#     CREATE TABLE users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dni VARCHAR (9) UNIQUE,
#         nombre VARCHAR (100),
#         edad INTEGER,
#         email VARCHAR(100)
#     )
# ''')

# users = [
#     ('1234', 'Nacho', 19, 'nacho@gmail.com'),
#     ('1235', 'Mario', 51, 'mario@gmail.com'),
#     ('1236', 'Mercedes', 38, 'mercedes@gmail.com'),
#     ('1237', 'Juan', 19, 'juan@gmail.com')
# ]

# cursor.executemany("INSERT INTO users VALUES (null, ?, ?, ?, ?)", users)

# cursor.execute("INSERT INTO users VALUES (null, '1237', 'Juan', 19, 'juan@gmail.com')")

conex.commit()
conex.close()