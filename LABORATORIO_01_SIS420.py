import random
def crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios):
# Se crea un mapa lleno de paredes
    mapa_laberinto = []
    numero_paredes_generadas = 0
    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
#             if (random.randrange(2) == 1 and numero_paredes_generadas < numero_paredes):
#                 fila_mapa_laberinto.append('#')
#                 numero_paredes_generadas += 1
#             else:
#                 fila_mapa_laberinto.append(' ')
            fila_mapa_laberinto.append('#')
        mapa_laberinto.append(fila_mapa_laberinto)
        
#Se ubica aleatoriamente un punto de inicio y a partir de ese punto se llenan espacios
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(numero_filas)
    columna_posicion_actual = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
    numero_espacios_generados += 1

#Se ubica una ficha de manera aleatoria
    ficha_fila = random.randrange(numero_filas)
    ficha_columnas = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = '$'

    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                columna_posicion_actual += 1
            
        if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
            mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = ' '
            numero_espacios_generados += 1
            
    return mapa_laberinto
numero_filas = int(input('Introduzca el número de filas del laberinto: '))
numero_columnas = int(input('Introduzca el número de columnas del laberinto: '))
numero_paredes = int(input('Introduzca el número de paredes del laberinto: '))
numero_espacios = numero_filas * numero_columnas - numero_paredes
laberinto = crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios)

for fila_mapa_laberinto in laberinto:
    print(fila_mapa_laberinto)
