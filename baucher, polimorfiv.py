from datetime import datetime

class MetodoPago:
    def procesar_pago(self, monto, nombre, dni):
        print("Procesando pago...")

    def generar_baucher(self, monto, nombre, dni, metodo):
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\nBAUCHER DE PAGO")
        print(f"Fecha y hora: {fecha_hora}")
        print(f"Nombre del cliente: {nombre}")
        print(f"DNI: {dni}")
        print(f"Método de pago: {metodo}")
        print(f"Monto pagado: ${monto:.2f}")
        print("Estado: Pago completado ")
        print("=====================================\n")


class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto, nombre, dni):
        print(f"Procesando pago con Tarjeta de Crédito por ${monto:.2f}...")
        self.generar_baucher(monto, nombre, dni, "Tarjeta de Crédito")


class PayPal(MetodoPago):
    def procesar_pago(self, monto, nombre, dni):
        print(f"Procesando pago con PayPal por ${monto:.2f}...")
        self.generar_baucher(monto, nombre, dni, "PayPal")


class Efectivo(MetodoPago):
    def procesar_pago(self, monto, nombre, dni):
        print(f"Procesando pago en efectivo por ${monto:.2f}...")
        self.generar_baucher(monto, nombre, dni, "Efectivo")


print("SISTEMA DE PAGO")

nombre = input("Ingrese su nombre: ")
dni = input("Ingrese su número de DNI: ")

print("\nSeleccione un método de pago:")
print("1. Tarjeta de Crédito")
print("2. PayPal")
print("3. Efectivo")

opcion = input("Opción (1-3): ")
monto = float(input("Ingrese el monto a pagar: "))

if opcion == "1":
    metodo = TarjetaCredito()
elif opcion == "2":
    metodo = PayPal()
elif opcion == "3":
    metodo = Efectivo()
else:
    print("Opción no válida.")
    metodo = None

if metodo:
    metodo.procesar_pago(monto, nombre, dni)
