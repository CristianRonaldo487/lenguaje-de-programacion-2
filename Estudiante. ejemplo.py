class Estudiante:
    def __init__(self, nombre, dni, codigo_estudiante):
        self.nombre = nombre
        self.dni = dni
        self.codigo = codigo_estudiante
        self.cursos = []
        
    def incribirse(self, curso):
        self.curso = curso
        curso.agregar_estudiante(self)

    def mostrar_informacion(self):
        print("\nEstudiante :{self.nombre} DNI: {self.dni} codigo :{self.codigo_estudiante}")
        print("Cursos inscritos: ")
        for curso in self.cursos:
            print(f"{curso.nombre_curso}")



class Profesor:
    def __init__(self,nombre,dni,especialidad):
        self.nombre = nombre
        self.dni = dni
        self.especialidad = especialidad

    def mostrar_informacion(self):
        print(f"Profesor: {self.nombre} DNI: {self.dni}, Especialidad {self.especialidad}")


class Curso:
    def __init__(self,nombre_curso,profesor):
        self.nombre_curso = nombre_curso
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            selfestudiante.append(estudiante)

    def mostrar_detalles(self):
        print(f"Curso : {self.nombre_curso}")
        print("profesor:")
        self.profesor.mostrar_informacion()
        print("Estudiantes inscritos: ")
        for est in self.estudiante:
            print("{est.nombre} {est.codigo_estudiante}")

class Universidad:
    def __init__(self,nombre):
        self.nombre = nombre
        self.cursos = []

    def agregar_cursos(self,curso):
        self cursos.append(curso)

    def mostrar_curso(self):
        curso.mostrar_detalles()
    
        
        






















        
    

    
    
