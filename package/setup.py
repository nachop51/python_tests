from setuptools import setup

setup(
    name="package",
    version="0.1",
    description="example package",
    author="nacho",
    author_email="nachoperalta0@gmail.com",
    url="https://github.com/Nachop51/",
    scripts=[],
    packages=["."]
)

# para instalar este paquete y poder acceder a el desde cualquier carpeta
# de la computadora es necesario correr este script asi
# python3 setup.py sdist
# cd dist
# pip install (nombre del archivo comprimido creado)