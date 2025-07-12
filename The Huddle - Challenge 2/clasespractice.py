# """
# 6. Clase Profesor y clase Clase (como materia). Un profesor puede dar muchas clases.
# ¿Cómo harías para que un profesor tenga una lista de las clases que da?
# """
# class Profesor:

#     def __init__(self, nombre, materias):
#         self.nombre = nombre
#         self.materias = materias

#     def agregar_materias(self, materia):
#         self.materias.append(materia)

#     def mostrar_materias(self):
#         print(f"\nEl profesor {self.nombre} tiene las siguientes materias: ")
#         for materia in self.materias:
#             print(materia, end=" ")

# maestro1 = Profesor("Edu", [])
# maestro1.agregar_materias("Matemática")
# maestro1.agregar_materias("Castellano")
# maestro1.agregar_materias("Inglés")
# maestro1.mostrar_materias()

# maestro2 = Profesor("Gustavo", [])
# maestro2.agregar_materias("Python")
# maestro2.agregar_materias("C++")
# maestro2.mostrar_materias()

"""
EJERCICIO OPCIONAL - RELACIÓN ENTRE OBJETOS
11. Clase Libro y clase Biblioteca
Una biblioteca puede tener muchos libros. Cada libro tiene título, autor y año de publicación.

✏️ Consigna:
Creá una clase Libro con los atributos mencionados.

Creá una clase Biblioteca que contenga una lista de libros.

Implementá métodos para: agregar un libro a la biblioteca, mostrar todos los libros, buscar libros por título.

Pregunta clave: ¿Cómo harías para que una biblioteca pueda administrar muchos libros distintos, sin mezclarlos ni perder control sobre la información?
"""
class Libro():

    def __init__(self, titulo, autor, año_de_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion

class Biblioteca:

    def __init__(self, libros):
        self.libros = libros

    def agregar_libros(self,libro):
        self.libros.append(libro)
        print(f"Has agregado {libro.titulo} de {libro.autor} ({libro.año_de_publicacion}) a la biblioteca")

    def mostrar_libros(self):
        print("La biblioteca tiene los siguientes libros: ")
        for libro in self.libros:
            print(f"- {libro.titulo} de {libro.autor} ({libro.año_de_publicacion})")

    def buscar_libros(self, pedido):
        for libro in self.libros:
            if libro.titulo.lower() == pedido.lower():
                print(f"Encontramos coincidencias con '{libro.titulo}'")
                return
        print("No encontramos el titulo solicitado")


## Registro de libros
registrar_libros = input("Quieres registrar algún libro? | Coloca Si o No ").lower()
if registrar_libros == "si":
    cantidad_libros = int(input("Ingresa cuantos libros quieres registrar"))
    libro_biblioteca = Biblioteca([])
    for libro in range(cantidad_libros):
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        año_de_publicacion = int(input("Año de Publicacion: "))
        nuevo_libro = Libro(titulo, autor, año_de_publicacion)
        libro_biblioteca.agregar_libros(nuevo_libro)
        print(f"Gracias por registrar '{titulo}' de {autor} ({año_de_publicacion})!")

mostrar_libros = input("Quieres ver los libros que hay en la Biblioteca? | Coloca Si o No ").lower()
if mostrar_libros == "si":
    libro_biblioteca.mostrar_libros()

## 
confirmacion_busqueda = input("Quieres buscar algun libro? | Coloca Si o No").lower()
if confirmacion_busqueda == "si":
    pedido_usuario = input("Busca un libro por su titulo: ")
    libro_biblioteca.buscar_libros(pedido_usuario)
else:
    print("Gracias por aportar a la Biblioteca! <3")
