# Programa para reservar un asiento en una sala de cine
# 0 = asiento libre
# 1 = asiento reservado

# Crear una matriz de 3 filas por 4 columnas
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar la fila y la columna del asiento
fila = int(input("Ingrese la fila (0 a 2): "))
columna = int(input("Ingrese la columna (0 a 3): "))

# Marcar el asiento como reservado
asientos[fila][columna] = 1

# Mostrar el estado de la sala
print("\nEstado de la sala:")

# Recorrer la matriz utilizando bucles anidados
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
