import numpy as np
import matplotlib.pyplot as plt

class Graficador:
    def __init__(self, x_min=-10, x_max=10, puntos=500):
        self.x_min = x_min
        self.x_max = x_max
        self.puntos = puntos
        self.funciones = []  

    def agregar(self, expr):
        self.funciones.append(expr)

    def graficar(self):
        x = np.linspace(self.x_min, self.x_max, self.puntos)
        plt.figure(figsize=(8,5))

        for expr in self.funciones:
            y = eval(expr, {"np": np, "x": x})
            plt.plot(x, y, label=expr)

        plt.axhline(0, color="black", linewidth=0.7)
        plt.axvline(0, color="black", linewidth=0.7)

        plt.legend()
        plt.grid(True)
        plt.show()

print("Graficador de funciones lineales")

g = Graficador(-10, 10, 1000)

f1 = input("Ingresa la primera función: ")
f2 = input("Ingresa la segunda función: ")

g.agregar(f1)
g.agregar(f2)


g.graficar()
