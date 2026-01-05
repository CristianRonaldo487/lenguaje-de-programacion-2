import numpy as np
import matplotlib.pyplot as plt

class Graficador:
    def __init__(self, x_min=-10, x_max=10, puntos=500):
        self.x_min = x_min
        self.x_max = x_max
        self.puntos = puntos
        self.funciones = []  # lista de funciones como strings

    def agregar(self, expr):
        """Agrega una función como string, ej: 'np.sin(x)', 'x**2', '2*x+3'"""
        self.funciones.append(expr)

    def graficar(self):
        x = np.linspace(self.x_min, self.x_max, self.puntos)
        plt.figure(figsize=(8,5))

        for expr in self.funciones:
            y = eval(expr, {"np": np, "x": x})
            plt.plot(x, y, label=expr)

        # Ejes X y Y
        plt.axhline(0, color="black", linewidth=0.7)
        plt.axvline(0, color="black", linewidth=0.7)

        plt.legend()
        plt.grid(True)
        plt.show()


# ---------------------------
# EJEMPLO DE USO
# ---------------------------
g = Graficador(-10, 10, 1000)
g.agregar("2*x+3")     # recta
g.agregar("x**2 - 4")  # parabola
g.graficar()
