class Graficador:
    def __init__(self, xmin=-10, xmax=10):
        self.xmin, self.xmax = xmin, xmax
        self.funciones = []

    def agregar(self, expr):
        self.funciones.append(expr)

    def graficar(self):
        for y in range(10, -11, -1):    
            linea = ""
            for x in range(self.xmin, self.xmax+1):
                simbolo = " "
                if x == 0 and y == 0: simbolo = "+"
                elif x == 0: simbolo = "|"
                elif y == 0: simbolo = "-"
                for f in self.funciones:
                    try:
                        if round(eval(f, {"x": x})) == y:
                            simbolo = "*"
                    except: pass
                linea += simbolo
            print(linea)
        for f in self.funciones: print("Función:", f)

g = Graficador(-10,10)
g.agregar(input("Función 1: "))
g.agregar(input("Función 2: "))
g.graficar()
