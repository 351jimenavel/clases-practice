### ESTE ESTÁ BIEN
class Mapa:

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [["." for _ in range(columnas)] for _ in range(filas)]
        self.entrada = None
        self.salida = None

    #--------métodos--------
    def colocar_entrada(self, fila_e, columna_e):
        self.matriz[fila_e][columna_e] = "E"
        self.entrada = (fila_e, columna_e)

    def colocar_salida(self, fila_s, columna_s):
        self.matriz[fila_s][columna_s] = "S"
        self.salida = (fila_s, columna_s)

    def colocar_obstaculos(self, fila, columna, tipo, cantidad):
        if self.coordenada_valida(fila, columna):
            if self.matriz[fila][columna] not in ["E", "S"]:
                for i in range(cantidad):
                    self.matriz[fila][columna] = tipo

    def coordenada_valida(self, fila, columna):
        return 0 <= fila < self.filas and 0 <= columna < self.columnas
    
    def mostrar_matriz(self):
        for x in self.matriz:
            print(" ".join(x))
        print()
        
    # Colocar esta funcion afuera (suelta)
    def celdas_diferentes(self):
        pass

def main():

    filas_usuario = int(input("Ingresa la cantidad de filas para el tablero: "))
    columnas_usuario = int(input("Ingresa la cantidad de columnas para el tablero: "))

    mapa = Mapa(filas_usuario,columnas_usuario)

    while True:

        coord_fila_entrada = int(input("Ingresa en que fila estará la ENTRADA: "))
        coord_columna_entrada = int(input("Ingresa en que columna estará la ENTRADA: "))

        coord_fila_salida = int(input("Ingresa en que fila estará la SALIDA: "))
        coord_columna_salida = int(input("Ingresa en que columna estará la SALIDA: "))
        
        if not mapa.coordenada_valida(coord_fila_entrada, coord_columna_entrada):
            print("Las coordenadas dadas para ENTRADA deben estar dentro del tablero")
            continue

        if not mapa.coordenada_valida(coord_fila_salida, coord_columna_salida):
            print("Las coordenadas dadas para SALIDA deben estar dentro del tablero")
            continue

        break
        
    mapa.colocar_entrada(coord_fila_entrada,coord_columna_entrada)
    mapa.colocar_salida(coord_fila_salida,coord_columna_salida)
    
    while True:
        print("Qué obstaculos quieres agregar")
        print("(1) Edificios. (2) Agua. (3) Muros. (4) Todos")
        eleccion_obstaculos_usuario = int(input("Elige: "))

        cantidad_maxima = int(input("Elige la cantidad de obstaculos que quieres agregar: "))
        coord_fila_obstaculo = int(input("Ingresa en que fila estará el obstaculo: "))
        coord_columna_obstaculo = int(input("Ingresa en que columna estará el obstaculo: "))

        if eleccion_obstaculos_usuario == 1:
            mapa.colocar_obstaculos(coord_fila_obstaculo, coord_columna_obstaculo, "X", cantidad_maxima)
            break
        elif eleccion_obstaculos_usuario == 2:
            mapa.colocar_obstaculos(coord_fila_obstaculo, coord_columna_obstaculo, "~", cantidad_maxima)
            break
        elif eleccion_obstaculos_usuario == 3: 
            mapa.colocar_obstaculos(coord_fila_obstaculo, coord_columna_obstaculo, "#", cantidad_maxima)
            break
        elif eleccion_obstaculos_usuario == 4: 
            mapa.colocar_obstaculos(coord_fila_obstaculo, coord_columna_obstaculo, "X", cantidad_maxima)
            mapa.colocar_obstaculos(coord_fila_obstaculo, coord_columna_obstaculo, "~", cantidad_maxima)
            mapa.colocar_obstaculos(coord_fila_obstaculo, coord_columna_obstaculo, "#", cantidad_maxima)
            break
        else:
            print("Solamente puedes elegir entre la opcion 1, 2, 3 o 4")
            continue

    mapa.mostrar_matriz()

if __name__ == '__main__':
    main()
