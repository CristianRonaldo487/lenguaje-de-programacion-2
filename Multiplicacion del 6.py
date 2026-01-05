class tablamultiplicar:
    def __init__(self, numero):
        self.numero = numero

    def generartabla(self):
        for i in range(1,11):
            resultado =self.numero*i
            print(f"{self.numero} * {i} = {resultado}")

def main():
    numero = int(input("ingrese el numero"))
    mitablamultiplicar = tablamultiplicar(numero)
    mitablamultiplicar.generartabla()

if __name__=="__main__":
    main()
