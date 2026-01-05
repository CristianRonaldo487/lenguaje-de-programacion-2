class Cuadrado:
    def area(self):
        lado = 5
        print(f"El area del cuadrado es: {lado * lado}")

class Triangulo:
    def area(self):
        base = 4
        altura = 6
        print(f"El area del triangulo es: {(base * altura) / 2}")

def calcular_area(figura):
    figura.area()

figuras = [Cuadrado(),Triangulo()]

for figura in figuras:
    calcular_area(figura)
    
