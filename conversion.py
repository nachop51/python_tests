multiplos = []

# Completa el ejercicio 
numero = int(input())
while numero < 0 or numero > 9:
    numero = int(input())
if numero == 0:
    multiplos = [0]
else:
    multiplos = list(range(0, 101, numero))

print(multiplos)