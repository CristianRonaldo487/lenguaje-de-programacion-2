class CalculadoraSuma:
    def __init__(self):
        self.total = 0

    def sumaNumeros(self):
        print("Calcular la suma de números ingresados")
        print("Escribe números para sumar. Escribe 'fin' para terminar")
        entrada = ""
        while entrada.lower() != "fin":
            entrada = input("Ingrese un número: ")
            if entrada.isdigit():
                numero = int(entrada)
                self.total += numero

                if numero % 2 == 0:
                    print(f"{numero} es PAR")
                else:
                    print(f"{numero} es IMPAR")

            elif entrada.lower() != "fin":
                print("Entrada inválida: escriba un número o 'fin'.")

        print(f"\nLa suma total es: {self.total}")


def main():
    calculadora = CalculadoraSuma()
    calculadora.sumaNumeros()


if __name__ == "__main__":
    main()
