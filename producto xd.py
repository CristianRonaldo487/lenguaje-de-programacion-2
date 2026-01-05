import gc

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"\nProducto registrado {self.nombre} - $ {self.precio} en stock {self.cantidad}")

    def mostrar_informacion(self):
        print(f"{self.nombre} precio $ {self.precio:.2f} en stock {self.cantidad}")

    def __del__(self):
        print(f"Producto eliminado: {self.nombre}")


inventario = []

n = int(input("¿Cuántos productos desea registrar? "))

for i in range(n):
    print(f"\nRegistro del producto {i+1}:")
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad en stock: "))

    producto = Producto(nombre, precio, cantidad)
    producto.mostrar_informacion()
    inventario.append(producto)

print("\n--- Inventario completo ---")
for producto in inventario:
    producto.mostrar_informacion()

inventario.clear()
gc.collect()
print("\nFin del programa")
