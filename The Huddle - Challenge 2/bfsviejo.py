from collections import deque
import time

def resolver_bfs(inicio_x, inicio_y, fin_x, fin_y, camino, matriz, mostrar_matriz):
    visitada = set()
    frontier = deque()
    solucion = {}

    frontier.append((inicio_x,inicio_y))    # Posicion inicial entra a la cola
    solucion[inicio_x,inicio_y] = None      # se marca que esa celda No tiene padre, ya que es el comienzo (no se llegó desde ni una celda)

    while frontier:
        x, y = frontier.popleft()       # celda actual 

        if matriz[x][y] == "S":
            break

        ## Se verifican celdas vecinas o adyacentes 
        if (x-1, y) in camino and (x - 1, y) not in visitada:   # no está fuera del tablero ni es obstáculo
            celda = (x-1, y)
            solucion[celda] = (x,y)

            frontier.append(celda)
            visitada.add((x-1, y))

            if matriz[celda[0]][celda[1]] not in ("E","S"):
                matriz[celda[0]][celda[1]] = "*"
        
            mostrar_matriz(matriz)
            time.sleep(0.1)

        if (x, y-1) in camino and (x, y-1) not in visitada:
            celda = (x, y-1)
            solucion[celda] = (x,y)

            frontier.append(celda)
            visitada.add((x, y-1))
            if matriz[celda[0]][celda[1]] not in ("E","S"):
                matriz[celda[0]][celda[1]] = "*"
        
            mostrar_matriz(matriz)
            time.sleep(0.1)

        if (x+1, y) in camino and (x+1, y) not in visitada:
            celda = (x+1, y)
            solucion[celda] = (x,y)

            frontier.append(celda)
            visitada.add((x+1, y))
            if matriz[celda[0]][celda[1]] not in ("E","S"):
                matriz[celda[0]][celda[1]] = "*"
        
            mostrar_matriz(matriz)
            time.sleep(0.1)

        if (x, y+1) in camino and (x, y+1) not in visitada:
            celda = (x, y+1)
            solucion[celda] = (x,y)

            frontier.append(celda)
            visitada.add((x, y+1))
            if matriz[celda[0]][celda[1]] not in ("E","S"):
                matriz[celda[0]][celda[1]] = "*"
        
            mostrar_matriz(matriz)
            time.sleep(0.1)
        
        if (fin_x, fin_y) not in solucion:
            return None
    # Devuelve el diccionario solucion que guarda la ruta recorrida (cada celda sabe desde dónde se llegó a ella).
    return solucion

