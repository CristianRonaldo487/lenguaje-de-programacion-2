class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        print(f"Curso creado: {self.nombre} ({self.codigo}) - Profesor: {self.profesor}")

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Código: {self.codigo}")
        print(f"Profesor: {self.profesor}")

    def __del__(self):
        print(f"Curso {self.nombre} eliminado.")


curso1 = Curso("Lenguaje de Programación II", "EST303", "Leonel Coyla Idme")

curso1.mostrar_informacion()
