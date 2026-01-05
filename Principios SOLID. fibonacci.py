# Principio S (Responsabilidad Única)
class GeneradorFibonacci:
    def generar(self):
        raise NotImplementedError("Debe implementar el método generar")


# Principios O y L
class FibonacciIterativo(GeneradorFibonacci):
    def __init__(self, n: int):
        self.n = n

    def generar(self):
        if self.n <= 0:
            return ()

        if self.n == 1:
            return (0,)

        # Tupla (no append)
        a, b = 0, 1
        serie = (a, b)

        for _ in range(2, self.n):
            a, b = b, a + b
            serie = serie + (b,)

        return serie


# Principio D (Inversión de Dependencias)
class Aplicacion:
    def __init__(self, generador: GeneradorFibonacci):
        self.generador = generador

    def ejecutar(self):
        resultado = self.generador.generar()
        print("Serie de Fibonacci:")
        print(resultado)


# Uso
fibonacci = FibonacciIterativo(10)
app = Aplicacion(fibonacci)
app.ejecutar()
