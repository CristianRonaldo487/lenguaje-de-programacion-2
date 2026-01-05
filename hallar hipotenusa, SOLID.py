import math

# Principio S
class FiguraGeometrica:
    def area(self):
        raise NotImplementedError("Debe implementar el area")

    def perimetro(self):
        raise NotImplementedError("Deve implementar el perimetro")

# Principios O y L
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    

class Rectangulo(FiguraGeometrica):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
        


# Principio D
class Aplicacion:
    def __init__(self, figura: FiguraGeometrica):
        self.figura = figura

    def ejecutar(self):
        print(f"Área: {self.figura.area()}")
        print(f"Perímetro: {self.figura.perimetro()}")

print("Circulo")
circulo = Circulo(5)
app1 = Aplicacion(circulo)
app1.ejecutar()

print("Rectangulo")
Rectangulo = Rectangulo (6, 3)
app2 = Aplicacion(Rectangulo)
app2.ejecutar()

