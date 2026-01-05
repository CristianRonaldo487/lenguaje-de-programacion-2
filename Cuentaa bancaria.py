class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar(self):
        print(f"Titular: {self.titular} Saldo: ${self.saldo:.2f}")

    def __sub__(self, cantidad):
        if isinstance(cantidad,(int,float)):
            if cantidad <= self. saldo:
                return CuentaBancaria(self.titular, self.saldo - cantidad)
            else:
                print("Fondos Insuficientes")
                return self

        else:
            print("operador no valido")
            return self

nombre = input("Ingrese el titular de la cuenta: ")
saldo_inicial = float(input("Ingrese el saldo inicial: "))            

cuenta1 = CuentaBancaria("Luis",1000)
cuenta1.mostrar()

cuenta2 = cuenta1 - 250
cuenta2.mostrar()

cuenta3 = cuenta2 - 1000
cuenta3.mostrar()
