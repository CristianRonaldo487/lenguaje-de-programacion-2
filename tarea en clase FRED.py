class Graficador:
    def __init__(self, xmin=-10, xmax=10, ymin=-10, ymax=10):
        self.xmin, self.xmax = xmin, xmax
        self.ymin, self.ymax = ymin, ymax
        self.funciones = []

    def agregar(self, expr, tipo="y"):
        """Tipo puede ser 'y' para y=f(x) o 'x' para x=f(y)"""
        self.funciones.append((expr, tipo))

    def evaluar_funcion(self, expr, tipo, x, y):
        try:
            if tipo == "y":
                # y = f(x)
                return round(eval(expr, {"x": x, "y": y})) == y
            else:
                # x = f(y)
                return round(eval(expr, {"x": x, "y": y})) == x
        except:
            return False

    def graficar(self):
        # Ajustar el rango de y para que coincida con la pantalla
        altura = 21  # líneas verticales
        ancho = self.xmax - self.xmin + 1
        
        for y_val in range(self.ymax, self.ymin - 1, -1):
            linea = ""
            for x_val in range(self.xmin, self.xmax + 1):
                simbolo = " "
                
                # Ejes coordenados
                if x_val == 0 and y_val == 0:
                    simbolo = "+"
                elif x_val == 0:
                    simbolo = "|"
                elif y_val == 0:
                    simbolo = "-"
                
                # Evaluar todas las funciones
                for expr, tipo in self.funciones:
                    if self.evaluar_funcion(expr, tipo, x_val, y_val):
                        simbolo = "*"
                        break
                
                linea += simbolo
            print(linea)
        
        # Mostrar las funciones
        for expr, tipo in self.funciones:
            print(f"Función: {tipo} = {expr}")

# Ejemplo de uso para el Ejercicio 1
print("=== EJERCICIO 1 ===")
g1 = Graficador(0, 15, 0, 15)
g1.agregar("15 - x", "y")  # y = 15 - x
g1.agregar("5", "x")       # x = 5 (recta vertical)
g1.graficar()

print("\n=== EJERCICIO 2 ===")
g2 = Graficador(0, 7, 0, 4)
g2.agregar("(20 - 3*x)/5", "y")  # 3x + 5y = 20
g2.graficar()

print("\n=== EJERCICIO 3 ===")
g3 = Graficador(0, 12, 0, 12)
g3.agregar("12 - x", "y")  # x + y = 12
g3.agregar("6", "y")       # y = 6
g3.agregar("4", "x")       # x = 4
g3.graficar()

print("\n=== EJERCICIO 4 ===")
g4 = Graficador(0, 9, 0, 6)
g4.agregar("(18 - 2*x)/3", "y")  # 2x + 3y = 18
g4.graficar()

print("\n=== EJERCICIO 5 ===")
g5 = Graficador(0, 10, 0, 5)
g5.agregar("(10 - x)/2", "y")  # x + 2y = 10
g5.graficar()
