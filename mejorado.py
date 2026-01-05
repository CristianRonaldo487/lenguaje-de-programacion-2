class Graficador:
    def __init__(self, xmin=-10, xmax=10, ymin=-10, ymax=10):
        self.xmin, self.xmax = xmin, xmax
        self.ymin, self.ymax = ymin, ymax
        self.funciones = []

    def agregar(self, expr):
        self.funciones.append(expr)

    def graficar(self):
        for y in range(self.ymax, self.ymin - 1, -1):
            linea = ""
            for x in range(self.xmin, self.xmax + 1):
                simbolo = " "
                if x == 0 and y == 0:
                    simbolo = "+"
                elif x == 0:
                    simbolo = "|"
                elif y == 0:
                    simbolo = "-"

                for expr in self.funciones:
                    try:
                        if round(eval(expr, {"x": x})) == y:
                            simbolo = "*"
                    except:
                        pass
                linea += simbolo
            print(linea)


# --------------------------
# Uso
# --------------------------
xmin = int(input("X mínimo: "))
xmax = int(input("X máximo: "))
ymin = int(input("Y mínimo: "))
ymax = int(input("Y máximo: "))

g = Graficador(xmin, xmax, ymin, ymax)

n = int(input("¿Cuántas funciones quieres graficar? "))
for i in range(n):
    expr = input(f"Función {i+1} (ejemplo: 2*x+3): ")
    g.agregar(expr)

print("\n--- Gráfico ASCII ---")
g.graficar()
