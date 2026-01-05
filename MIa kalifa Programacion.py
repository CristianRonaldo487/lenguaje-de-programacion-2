class Graficador:
    def __init__(self, x_min=-10, x_max=10, puntos=21):
        self.x_min = x_min
        self.x_max = x_max
        self.puntos = puntos
        self.funciones = []

    def agregar(self, expr):
        self.funciones.append(expr)

    def graficar(self):
        # Generar valores de x enteros en el rango
        valores_x = list(range(self.x_min, self.x_max + 1))

        # Evaluar cada funcion
        resultados = []
        for expr in self.funciones:
            y_vals = []
            for x in valores_x:
                try:
                    y = eval(expr, {"x": x})
                    y_vals.append(y)
                except Exception:
                    y_vals.append(None)
            resultados.append((expr, y_vals))

        # Graficar en texto (ASCII)
        y_min = -10
        y_max = 10
        for y in range(y_max, y_min - 1, -1):
            linea = ""
            for i, x in enumerate(valores_x):
                simbolo = " "
                if x == 0 and y == 0:
                    simbolo = "+"  # origen
                elif x == 0:
                    simbolo = "|"  # eje Y
                elif y == 0:
                    simbolo = "-"  # eje X

                for expr, y_vals in resultados:
                    if y_vals[i] == y:
                        simbolo = "*"

                linea += simbolo
            print(linea)

        # Mostrar qué funciones se graficaron
        for expr, _ in resultados:
            print("Función:", expr)


# Uso del programa
print("Graficador de funciones (ASCII, sin librerías)")

g = Graficador(-10, 10, 21)

f1 = input("Ingresa la primera función (ej: x**2, x+2, -x): ")
f2 = input("Ingresa la segunda función: ")

g.agregar(f1)
g.agregar(f2)

g.graficar()
