
class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, stock: int = 0):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

#Encapsulamiento 
    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

#Acciones del objeto
    def aumentar_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__stock += cantidad

    def disminuir_stock(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__stock:
            raise ValueError("Stock insuficiente")
        self.__stock -= cantidad


class InventarioRepository:
    def __init__(self):
        self.__productos = {}

    def agregar(self, producto: Producto):
        self.__productos[producto.get_codigo()] = producto

    def obtener(self, codigo: str):
        return self.__productos.get(codigo)

    def listar(self):
        return self.__productos.values()
    
#Principio SOLID: separación de responsabilidades


class InventarioService:
    def __init__(self, repositorio: InventarioRepository):
        self.__repositorio = repositorio

    def registrar_producto(self, producto: Producto):
        if self.__repositorio.obtener(producto.get_codigo()):
            raise ValueError("El producto ya existe")
        self.__repositorio.agregar(producto)

    def entrada_stock(self, codigo: str, cantidad: int):
        producto = self.__repositorio.obtener(codigo)
        if not producto:
            raise ValueError("Producto no encontrado")
        producto.aumentar_stock(cantidad)

    def salida_stock(self, codigo: str, cantidad: int):
        producto = self.__repositorio.obtener(codigo)
        if not producto:
            raise ValueError("Producto no encontrado")
        producto.disminuir_stock(cantidad)

    def obtener_inventario(self):
        return self.__repositorio.listar()



class ReporteService:
    def generar_reporte(self, productos):
        print("\nREPORTE DE INVENTARIO")
        print("-" * 55)
        print(f"{'Código':<10}{'Producto':<20}{'Stock':<10}{'Precio':<10}")
        print("-" * 55)
        for p in productos:
            print(
                f"{p.get_codigo():<10}"
                f"{p.get_nombre():<20}"
                f"{p.get_stock():<10}"
                f"S/. {p.get_precio():<10}"
            )
        print("-" * 55)


def main():
    repositorio = InventarioRepository()
    inventario = InventarioService(repositorio)
    reporte = ReporteService()

    while True:
        print("\nSISTEMA DE INVENTARIO")
        print("1. Registrar producto")
        print("2. Entrada de stock")
        print("3. Salida de stock")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                producto = Producto(codigo, nombre, precio)
                inventario.registrar_producto(producto)
                print("Producto registrado correctamente")

            elif opcion == "2":
                codigo = input("Código del producto: ")
                cantidad = int(input("Cantidad a ingresar: "))
                inventario.entrada_stock(codigo, cantidad)
                print("Stock actualizado")

            elif opcion == "3":
                codigo = input("Código del producto: ")
                cantidad = int(input("Cantidad a retirar: "))
                inventario.salida_stock(codigo, cantidad)
                print("Stock actualizado")

            elif opcion == "4":
                productos = inventario.obtener_inventario()
                reporte.generar_reporte(productos)

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida")

        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    main()
