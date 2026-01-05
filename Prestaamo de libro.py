class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")


class Prestamo:
    def __init__(self, libro, fecha_prestamo):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.devuelto = False

    def marcar_devolucion(self):
        self.devuelto = True
        self.libro.devolver()  

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []  

    def realizar_prestamo(self, libro, fecha):
        if libro.disponible:
            libro.prestar()
            prestamo = Prestamo(libro, fecha)
            self.prestamos.append(prestamo)
        else:
            print("No se puede realizar el préstamo del libro. NO DISPONIBLE.")

    def mostrar_prestamos(self):
        print(f"\nPréstamos de {self.nombre}:")
        for p in self.prestamos:
            estado = 'devuelto' if p.devuelto else 'pendiente'
            print(f"- {p.libro.titulo} | Estado: {estado} | Fecha: {p.fecha_prestamo}")


def main():
    libro_1 = Libro("Cien años de soledad", "Gabriel García Márquez", "12345")
    libro_2 = Libro("El principito", "Antoine de Saint-Exupéry", "98765")

    usuario_1 = Usuario("Juan Pérez", "483762")

    usuario_1.realizar_prestamo(libro_1, "2025-10-13")
    usuario_1.mostrar_prestamos()

    usuario_1.prestamos[0].marcar_devolucion()
    usuario_1.mostrar_prestamos()


if __name__ == "__main__":
    main()
