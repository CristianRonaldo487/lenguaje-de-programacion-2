from abc import ABC, abstractmethod

# Principio S 
class Operacion(ABC):
    @abstractmethod
    def calcular(self):
        pass


# Principio O y L
class Suma(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a + self.b


class Resta(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a - self.b


class Multiplicacion(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a * self.b


class Division(Operacion):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        if self.b == 0:
            raise ValueError("No se puede dividir entre cero")
        return self.a / self.b


# Principio D
class Aplicacion:
    def __init__(self, operacion: Operacion):
        self.operacion = operacion

    def ejecutar(self):
        return self.operacion.calcular()

def main():
    print("CALCULADORA SOLID")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicación")
    print("4.División")

    opcion = input("Elige una opción: ")

    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            operacion = Suma(a, b)
        elif opcion == "2":
            operacion = Resta(a, b)
        elif opcion == "3":
            operacion = Multiplicacion(a, b)
        elif opcion == "4":
            operacion = Division(a, b)
        else:
            print("Opción inválida")
            return

        app = Aplicacion(operacion)
        resultado = app.ejecutar()
        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")


main()
