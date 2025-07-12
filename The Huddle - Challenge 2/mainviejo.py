import time
import os
from bfsviejo import resolver_bfs

#________________________________________________CONFIG. INICIALES________________________________________________
fila_tablero = int(input("Ingresa la cantidad de filas para tu tablero inicial: "))
columna_tablero = int(input("Ingresa la cantidad de columnas para tu tablero inicial: "))
matriz = [["." for _ in range(columna_tablero)] for _ in range(fila_tablero)]

#________________________________________________FUNCIONES PRINCIPALES_______________________________________________
def limpiar_consola():
    '''Funcion para limpiar la terminal, así se simula un solo tablero'''
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_matriz(elemento):
    '''Funcion para mostrar la matriz ordenada'''
    limpiar_consola()
    for x in elemento:
        print(" ".join(x))
    print()

def coordenada_valida(fila, columna):
    '''Funcion que describe los parámetros de validez dentro del tablero'''
    return 0 <= fila < fila_tablero and 0 <= columna < columna_tablero

def pedir_coordenadas(texto):
    '''Función para solicitar al usuario fila/columna de diferentes elementos dentro del tablero'''
    fila = int(input(f"Ingresa en que fila estará{texto}: "))
    columna = int(input(f"Ingresa en que columna estará{texto}: "))

    return fila, columna

def celdas_diferentes(f1, f2, c1, c2):
    '''Funcion que describe como deben estar filas y columnas entre ellas mismas'''
    return f1 != f2 or c1 != c2

#________________________________________________CONFIG. ENTRADA Y SALIDA________________________________________________
while True:
    
    coord_fila_entrada, coord_columna_entrada = pedir_coordenadas(" la ENTRADA")
    coord_fila_salida, coord_columna_salida = pedir_coordenadas(" la SALIDA")

    if not coordenada_valida(coord_fila_entrada, coord_columna_entrada):
        print("Las coordenadas dadas para ENTRADA deben estar dentro del tablero")
        continue

    if not coordenada_valida(coord_fila_salida, coord_columna_salida):
        print("Las coordenadas dadas para SALIDA deben estar dentro del tablero")
        continue
        
    if not celdas_diferentes(coord_fila_entrada, coord_fila_salida, coord_columna_entrada, coord_columna_salida):
        print("Entrada y Salida no pueden ser iguales")
        continue

    break 

matriz[coord_fila_entrada][coord_columna_entrada] = "E"
matriz[coord_fila_salida][coord_columna_salida] = "S"
mostrar_matriz(matriz)
time.sleep(1)

#________________________________________________OBSTÁCULOS________________________________________________
obstaculos = []
edificios = []
baches = []
muros = []

def configuracion_edificios():
    '''Función que describe las validaciones del obstaculo "Edificio" y como se verá'''
    global matriz

    for i in range(cantidad_maxima_edificios):
        while True:
            fila_obstaculo, columna_obstaculo = pedir_coordenadas(f" el EDIFICIO N°{i+1}")
            if not coordenada_valida(fila_obstaculo, columna_obstaculo):
                print("Las coordenadas de EDIFICIO deben estar dentro del tablero")
                continue

            if (fila_obstaculo, columna_obstaculo) in obstaculos:
                print("Ya hay un edificio ahí")
                continue

            if (fila_obstaculo, columna_obstaculo) == (coord_fila_entrada, coord_columna_entrada) or (fila_obstaculo, columna_obstaculo) == (coord_fila_salida, coord_columna_salida):
                print("No podes poner un edificio sobre la entrada o salida")
                continue
            
            edificios.append((fila_obstaculo, columna_obstaculo))
            obstaculos.append((fila_obstaculo,columna_obstaculo))
            break
    for fila_edificio, columna_edificio in edificios:
        matriz[fila_edificio][columna_edificio] = "X"
        mostrar_matriz(matriz)
        time.sleep(0.5)

def configuracion_agua():
    '''Función que describe las validaciones del obstaculo "Agua/Bache" y como se verá'''

    global matriz

    for i in range(cantidad_maxima_agua):
        while True:
            fila_obstaculo, columna_obstaculo = pedir_coordenadas(f" el BACHE N°{i+1}")
            if not coordenada_valida(fila_obstaculo, columna_obstaculo):
                print("Las coordenadas de BACHE deben estar dentro del tablero")
                continue

            if (fila_obstaculo, columna_obstaculo) in obstaculos:
                print("Ya hay algo ahí")
                continue

            if (fila_obstaculo, columna_obstaculo) == (coord_fila_entrada, coord_columna_entrada) or (fila_obstaculo, columna_obstaculo) == (coord_fila_salida, coord_columna_salida):
                print("No podes poner un bache sobre la entrada o salida")
                continue

            baches.append((fila_obstaculo,columna_obstaculo))
            obstaculos.append((fila_obstaculo,columna_obstaculo))
            break

    for fila_baches, columna_baches in baches:
        matriz[fila_baches][columna_baches] = "~"
        mostrar_matriz(matriz)
        time.sleep(0.5)

def configuracion_muros():
    '''Función que describe las validaciones del obstaculo "Muro" y como se verá'''

    global matriz
    for i in range(cantidad_maxima_muros):
        while True:
            fila_obstaculo, columna_obstaculo = pedir_coordenadas(f" el MURO N°{i+1}")
            if not coordenada_valida(fila_obstaculo, columna_obstaculo):
                print("Las coordenadas de MURO deben estar dentro del tablero")
                continue

            if (fila_obstaculo, columna_obstaculo) in obstaculos:
                print("Ya hay algo ahí")
                continue

            if (fila_obstaculo, columna_obstaculo) == (coord_fila_entrada, coord_columna_entrada) or (fila_obstaculo, columna_obstaculo) == (coord_fila_salida, coord_columna_salida):
                print("No podes poner un muro sobre la entrada o salida")
                continue
            
            matriz[fila_obstaculo][columna_obstaculo] = "#"
            mostrar_matriz(matriz)
            time.sleep(0.5)
            muros.append((fila_obstaculo,columna_obstaculo))
            obstaculos.append((fila_obstaculo,columna_obstaculo))
            break

#________________________________________________USUARIO INGRESA ELEMENTOS________________________________________________
while True:
    print("Qué obstaculos quieres agregar")
    print("(1) Edificios. (2) Agua. (3) Muros. (4) Todos")
    eleccion_obstaculos_usuario = int(input("Elige: "))

    if eleccion_obstaculos_usuario == 1:
        cantidad_maxima_edificios = int(input("Elige la cantidad de edificios que quieres agregar: "))
        configuracion_edificios()
        break
    elif eleccion_obstaculos_usuario == 2:
        cantidad_maxima_agua = int(input("Elige la cantidad de baches que quieres agregar: "))
        configuracion_agua()
        break
    elif eleccion_obstaculos_usuario == 3: 
        cantidad_maxima_muros = int(input("Elige la cantidad de muros que quieres agregar: "))
        configuracion_muros()
        break
    elif eleccion_obstaculos_usuario == 4: 
        cantidad_maxima_edificios = int(input("Elige la cantidad de edificios que quieres agregar: "))
        configuracion_edificios()
        cantidad_maxima_agua = int(input("Elige la cantidad de baches que quieres agregar: "))
        configuracion_agua()
        cantidad_maxima_muros = int(input("Elige la cantidad de muros que quieres agregar: "))
        configuracion_muros()
        break
    else:
        print("Solamente puedes elegir entre la opcion 1, 2, 3 o 4")
        continue

# Recolecta todas las celdas disponibles para caminar (celdas libres)
camino = []
for fila in range(fila_tablero):
    for columna in range(columna_tablero):
        if matriz[fila][columna] in [".", "E", "S"]:
            camino.append((fila, columna))

#_________________________________________BACKTRACKING__________________________________________
def backtracking(x,y):
    '''Función que sirve para reconstruir el camino que BFS encontró desde la salida (S) hacia la entrada (E), usando el diccionario solucion.'''

    while (x,y) != (coord_fila_entrada, coord_columna_entrada): #Mientras no hayas llegado a la entrada, seguís retrocediendo.
        if matriz[x][y] not in ("E","S"):
            matriz[x][y] = "o"
            mostrar_matriz(matriz)
            time.sleep(0.2)
        x,y = solucion[(x,y)]   # Busca en el diccionario solucion cuál fue la celda anterior desde donde llegó a (x, y) cuando BFS exploró. Luego, actualiza (x, y) para retroceder por ese camino.

#________________________________________TABLERO COMPLETO________________________________________

print("Tablero final configurado: ")
mostrar_matriz(matriz)

#_______________________________________LÓGICA DEL ALGORITMO_______________________________________

solucion = resolver_bfs(coord_fila_entrada, coord_columna_entrada, coord_fila_salida, coord_columna_salida, camino, matriz, mostrar_matriz)

if solucion is None:
    print("No se encontró un camino posible que una Entrada y Salida")
else:
    backtracking(coord_fila_salida, coord_columna_salida)