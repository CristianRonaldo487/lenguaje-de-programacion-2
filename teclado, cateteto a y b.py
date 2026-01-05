from typing import TypeVar
import math

T = TypeVar('T', int, float)

def calcular_hipotenusa(cateto_a: T, cateto_b: T) -> T:
    return math.sqrt(cateto_a**2 + cateto_b**2)

def main():
    try:
        a = float(input("Ingrese el valor del cateto A: "))
        b = float(input("Ingrese el valor del cateto B: "))

        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser positivos.")

        hip = calcular_hipotenusa(a, b)
        print("Hipotenusa =", hip)

    except ValueError as ve:
        print("Error:", ve)


if __name__ == "__main__":
    main()
