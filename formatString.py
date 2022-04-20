v = "otro texto"
n = 10 
print("Un texto",v, "y un número",n)

c = "Un texto '{}' y un número '{}'".format(v,n) 
print(c)

print("Un texto '{0}' y un número '{1}'".format(v,n))
print("Un texto '{1}' y un número '{0}'".format(v,n))
print("Un texto '{v}' y un número '{n}'".format(n=n, v=v))
print("{v},{v},{v}".format(v=v))
print("{:>30}".format("palabra"))
# se crean espacios a la derecha de la palabra si no es de 30 caracteres
print("{:30}".format("palabra"))
# centrado entre 30 espacios
print("{:^30}".format("palabra"))
# trunc
print("{:.5}".format("palabra"))
# alineamiento a la derecha y trunc
print("{:>30.3}".format("palabra"))
# alineamiento de numeros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))
# formateo de decimales
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))
# f-strings
texto = "Hola mundo"
print(f"{texto:40}")
print(f"{texto:>40}")
print(f"{texto:^40}")
limite = 4
print(f"{texto:.{limite}}")
longitud = 30
print(f"{texto:>30.4}")
print(f"{texto:<30.4}")
print(f"{texto:^30.4}")
print(f"{texto:>{longitud}.{limite}}")
print(f"{texto:<{longitud}.{limite}}")
print(f"{texto:^{longitud}.{limite}}")
print(f"{1:6d}")
print(f"{10:6d}")
print(f"{100:6d}")
print(f"{1000:6d}")
print(f"{10000:6d}")
print(f"{100000:6d}")
print(f"{1:06d}")
print(f"{10:06d}")
print(f"{100:06d}")
print(f"{1000:06d}")
print(f"{10000:06d}")
print(f"{100000:06d}")
print(f"{3.1415926:7.3f}")
print(f"{153.21:7.3f}")
numero = 3.1415926
longitud = 21
decimales = 10
print(f"{numero:0{longitud}.{decimales}f}")