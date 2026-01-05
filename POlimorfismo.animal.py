class animal:
    def __init__(self):
        print("Sonido Generico")

class perro(animal):
    def hacer_sonido(self):
        print("Guau")

class gato(animal):
    def hacer_sonido(self):
        print("Miau")


animales = [perro(), gato(), animal()]
for animal in animales:
    animal.hacer_sonido

    
