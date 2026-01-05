class Persona:
    def __init__(self,nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola soy {self.nombre}")
        
persona1 = Persona("Carlos")
Persona1.saludar()

Persona2 = Persona("Coaguila")
Persona2.saludar()
