import gc

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro registrado: {self.titulo} de {self.autor}, {self.anio}")

    def mostrar_informacion(self):
        print(f"'{self.titulo}' fue escrito por {self.autor} en {self.anio}")

    def __del__(self):
        print(f"Libro eliminado: {self.titulo}")


biblioteca = []

n = int(input("¿Cuántos libros desea registrar? "))

for i in range(n):
    print(f"\n Registro del libro {i+1}:")
    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))
    
    libro = Libro(titulo, autor, anio)
    libro.mostrar_informacion()
    biblioteca.append(libro)

print("\n Biblioteca completa ---")
for libro in biblioteca:
    libro.mostrar_informacion()

biblioteca.clear()
gc.collect()
print("Fin del programa")



