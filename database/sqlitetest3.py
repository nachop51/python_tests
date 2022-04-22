import sqlite3

conex = sqlite3.connect("db3.db")
cursor = conex.cursor()

# sintaxis para uso de WHERE
# cursor.execute("SELECT * FROM productos WHERE id=1")
# users = cursor.fetchone()
# print(users)

# sintaxis para actualizar un producto
cursor.execute("UPDATE productos SET precio=20.00 WHERE id=1")

# cursor.execute("INSERT INTO productos VALUES (null, 'TV', 'TV', 150)")
# sintaxis para borrar un producto
# cursor.execute("DELETE FROM productos WHERE nombre='TV'")

conex.commit()
conex.close()