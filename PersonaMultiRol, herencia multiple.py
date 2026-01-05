class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario

    def trabajar(self):
        print(f"Estoy trabajando como {self.profesion} y gano ${self.salario}.")


class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad

    def estudiar(self):
        print(f"Estudio {self.carrera} en la universidad {self.universidad}.")


class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def mostrar_informacion(self):
        print("===== Información de la Persona =====")
        self.presentarse()
        self.trabajar()
        self.estudiar()


def main():
    persona1 = PersonaMultirol(
        nombre="Raiza",
        edad=19,
        profesion="informatico",
        salario=10200,
        carrera="ING. Estadistia e Informatica",
        universidad="Nacional del Altiplano"
    )
    persona1.mostrar_informacion()
    persona2 = PersonaMultirol(
        nombre= "Dilan",
        edad=19,
        profesion="Nutricion Robotica",
        salario=1000000000000000,
        carrera="ingenieria aeroespacial",
        universidad= " Cesar vallejo",
        )
    persona2.mostrar_informacion()


if __name__ == "__main__":
    main()
