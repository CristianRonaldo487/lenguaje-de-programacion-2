class CalculadoraSuma:
    def __init__(self):
        self.total = 0

    def sumaNumeros(self):
        print("calcular la suma de numeros ingresado")
        print("Escribe numeros parea sumar. Escribe ´fin´ para terminar")
        entrada=""
        while entrada.lower() != "fin":
            entrada = input("ingrese un numero : ")
            if entrada.isdigit():
                self.total+= int(entrada)

            elif entrada.lower()!= "fin":
                print("Entrada invalida: Escriba un numero o ´fin´ ")
        print(f"La suma total es: {self.total}")


def main():
    calculadora = CalculadoraSuma()

    calculadora.sumaNumeros()
    
if __name__=="__main__":
    main()
            
              
