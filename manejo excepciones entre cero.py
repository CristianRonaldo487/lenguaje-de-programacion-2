class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dividir(self):
        try:
            resultado = self.a / self.b
            return resultado
        except ZeroDivisionError:
            return "error: No se puede dividir entre cero."
        except Exception as e:
            return f"ocurrio un error: {e}"
        finally:
            print("operación finalizada")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))            


operacion = Division(10, 0) 
print(operacion.dividir())

        
