from typing import TypeVar

T = TypeVar('T', int, float)

class calcular_area

    

    def calcular_factorial(self) -> int:
        n = int(self.numero)

        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


def main():
    try:
        n = float(input("Ingrese un número: "))
        cal = CalculadoraFactorial(n)
        print(f"El factorial de {int(n)} es: {cal.calcular_factorial()}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
