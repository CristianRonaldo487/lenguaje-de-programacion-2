class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        print(f"Curso creado: {self.nombre} ({self.codigo}) - Profesor: {self.profesor}")
