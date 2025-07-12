class Mapa:

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [["." for _ in range(columnas)] for _ in range(filas)]
        self.entrada = None
        self.salida = None

    def mostrar_matriz(self):
        for x in self.matriz:
            print(" ".join(x))
        print()

    def coordenada_valida(self, fila, columna):
        return 0 <= fila < self.filas and 0 <= columna < self.columnas

    def colocar_entrada(self, fila_e, columna_e):
        self.matriz[fila_e][columna_e] = "E"

    def colocar_salida(self, fila_s, columna_s):
        self.matriz[fila_s][columna_s] = "S"

    # Colocar esta funcion afuera (suelta)
    def celdas_diferentes(self):
        pass

filas_usuario = int(input("Ingresa la cantidad de filas para el tablero: "))
columnas_usuario = int(input("Ingresa la cantidad de columnas para el tablero: "))

coord_fila_entrada = int(input("Ingresa en que fila estará la ENTRADA"))
coord_columna_entrada = int(input("Ingresa en que columna estará la ENTRADA"))

coord_fila_salida = int(input("Ingresa en que fila estará la SALIDA"))
coord_columna_salida = int(input("Ingresa en que columna estará la SALIDA"))

mapa = Mapa(filas_usuario,columnas_usuario)
mapa.colocar_entrada(coord_fila_entrada,coord_columna_entrada)
mapa.colocar_salida(coord_fila_salida,coord_columna_salida)
mapa.mostrar_matriz()