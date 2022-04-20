matriz = [
    [8, 7, 0],
    [34, 2, -1],
    [5, -5, 12]
]

# Completa el ejercicio aquí
for i, v in enumerate(matriz):
    for j, val in enumerate(matriz[i]):
        if val % 2 == 0:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 1

print(matriz)