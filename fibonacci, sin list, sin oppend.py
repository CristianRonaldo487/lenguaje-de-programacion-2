def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def main():
    try:
        n = int(input("¿Cuantos terminos quieres mostrar?: "))
        if n <= 0:
            raise ValueError("Debes ingresar un numero entero positivo.")

        print("\nSerie de Fibonacci:")
        fibonacci(n)

    except ValueError as ve:
        print("Error:", ve)

if __name__ == "__main__":
    main()
