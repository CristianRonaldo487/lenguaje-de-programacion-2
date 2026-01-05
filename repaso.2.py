class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = valor

    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            self._precio -= self._precio * (porcentaje / 100)
        else:
            print("Descuento inválido")

# ---- PRUEBA ----
p = Producto("Laptop", 2000)
print(p.precio)

p.aplicar_descuento(10)
print(p.precio)

p.aplicar_descuento(200)   # inválido
