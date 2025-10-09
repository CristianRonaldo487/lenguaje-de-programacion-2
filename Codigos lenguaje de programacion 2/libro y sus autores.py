import gc

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro registrado: {self.titulo}, {self.autor}, {self.anio}")

    def mostrar_informacion(self):
        print(f"'{self.titulo}' fue escrito por {self.autor} en {self.anio}")

    def __del__(self):
        print(f"Libro eliminado: {self.titulo}")

n = int(input("¿Cuántos libros deseas registrar? "))

datos_libros = []
for i in range(n):
    print(f"\n--- Registro de libros {i+1} ---")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    anio = input("Anio: ")
    libro = Libro(titulo, autor, anio)
    datos_libros.append(libro)

biblioteca = []
for libro in datos_libros:
    libro.mostrar_informacion()
    biblioteca.append(libro)

biblioteca.clear()
del libro
gc.collect()

print("\nFin del programa")
