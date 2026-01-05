import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime
import os

# ===============================
# MODELO
# ===============================
class Producto:
    def __init__(self, codigo, nombre, precio, stock=0):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    def aumentar_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("¡La cantidad debe ser mayor que 0!")
        self.__stock += cantidad

    def disminuir_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("¡La cantidad debe ser mayor que 0!")
        if cantidad > self.__stock:
            raise ValueError("¡No hay suficiente stock!")
        self.__stock -= cantidad


# ===============================
# REPOSITORIO
# ===============================
class InventarioRepository:
    def __init__(self):
        self.__productos = {}

    def agregar(self, producto):
        self.__productos[producto.get_codigo()] = producto

    def obtener(self, codigo):
        return self.__productos.get(codigo)

    def listar(self):
        return self.__productos.values()


# ===============================
# SERVICIO
# ===============================
class InventarioService:
    def __init__(self, repo):
        self.__repo = repo

    def registrar_producto(self, producto):
        if self.__repo.obtener(producto.get_codigo()):
            raise ValueError("¡Ese producto ya existe!")
        self.__repo.agregar(producto)

    def entrada_stock(self, codigo, cantidad):
        producto = self.__repo.obtener(codigo)
        if not producto:
            raise ValueError("¡Producto no encontrado!")
        producto.aumentar_stock(cantidad)

    def salida_stock(self, codigo, cantidad):
        producto = self.__repo.obtener(codigo)
        if not producto:
            raise ValueError("¡Producto no encontrado!")
        producto.disminuir_stock(cantidad)

    def obtener_inventario(self):
        return self.__repo.listar()


# ===============================
# INTERFAZ INFANTIL
# ===============================
class InventarioGalenoKids:
    def __init__(self, root):
        self.root = root
        self.root.title("🎒 Inventario Feliz - Academia Galeno")
        self.root.geometry("920x580")
        self.root.configure(bg="#FFF176")

        self.repo = InventarioRepository()
        self.service = InventarioService(self.repo)

        self.crear_interfaz()

    def crear_interfaz(self):
        # TÍTULO
        titulo = tk.Label(
            self.root,
            text="🎨 ACADEMIA DINOREX 🎨\n📦 Inventario Feliz 📦",
            bg="#FF4081",
            fg="white",
            font=("Comic Sans MS", 24, "bold"),
            pady=10
        )
        titulo.pack(fill=tk.X)

        # FORMULARIO
        form = tk.Frame(self.root, bg="#FFF9C4")
        form.pack(pady=10)

        textos = ["🆔 Código", "🧸 Nombre", "💰 Precio", "📦 Cantidad"]
        self.entradas = []

        for i, t in enumerate(textos):
            tk.Label(
                form, text=t,
                bg="#FFF9C4",
                font=("Comic Sans MS", 14)
            ).grid(row=i, column=0, sticky="e", pady=5)

            e = tk.Entry(form, font=("Comic Sans MS", 14), width=22)
            e.grid(row=i, column=1, pady=5)
            self.entradas.append(e)

        self.codigo, self.nombre, self.precio, self.cantidad = self.entradas

        # BOTONES
        botones = tk.Frame(self.root, bg="#FFF176")
        botones.pack(pady=10)

        tk.Button(
            botones, text="➕ Agregar",
            bg="#4CAF50", fg="white",
            font=("Comic Sans MS", 14),
            width=15, command=self.registrar
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            botones, text="📥 Entrar",
            bg="#03A9F4", fg="white",
            font=("Comic Sans MS", 14),
            width=15, command=self.entrada
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            botones, text="📤 Sacar",
            bg="#FF5722", fg="white",
            font=("Comic Sans MS", 14),
            width=15, command=self.salida
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            botones, text="👀 Ver Todo",
            bg="#9C27B0", fg="white",
            font=("Comic Sans MS", 14),
            width=15, command=self.mostrar
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            botones, text="🖨️ Imprimir",
            bg="#FF9800", fg="white",
            font=("Comic Sans MS", 14),
            width=15, command=self.imprimir_reporte
        ).grid(row=1, column=1, columnspan=2, pady=10)

        # TABLA
        self.tabla = ttk.Treeview(
            self.root,
            columns=("codigo", "nombre", "stock", "precio"),
            show="headings",
            height=8
        )

        self.tabla.heading("codigo", text="Código")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("stock", text="Stock")
        self.tabla.heading("precio", text="Precio")

        self.tabla.pack(fill=tk.X, padx=20, pady=10)

    # ===============================
    # FUNCIONES
    # ===============================
    def registrar(self):
        try:
            producto = Producto(
                self.codigo.get(),
                self.nombre.get(),
                float(self.precio.get())
            )
            self.service.registrar_producto(producto)
            messagebox.showinfo("😊", "¡Producto agregado!")
        except Exception as e:
            messagebox.showerror("😢 Error", str(e))

    def entrada(self):
        try:
            self.service.entrada_stock(
                self.codigo.get(),
                int(self.cantidad.get())
            )
            messagebox.showinfo("🎉", "¡Entraron productos!")
        except Exception as e:
            messagebox.showerror("😢 Error", str(e))

    def salida(self):
        try:
            self.service.salida_stock(
                self.codigo.get(),
                int(self.cantidad.get())
            )
            messagebox.showinfo("👍", "¡Productos retirados!")
        except Exception as e:
            messagebox.showerror("😢 Error", str(e))

    def mostrar(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for p in self.service.obtener_inventario():
            self.tabla.insert(
                "", "end",
                values=(
                    p.get_codigo(),
                    p.get_nombre(),
                    p.get_stock(),
                    f"S/ {p.get_precio():.2f}"
                )
            )

    def imprimir_reporte(self):
        productos = list(self.service.obtener_inventario())

        if not productos:
            messagebox.showwarning("😯", "No hay productos para imprimir")
            return

        archivo = "reporte_inventario_galeno.pdf"
        fecha = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

        c = canvas.Canvas(archivo, pagesize=A4)
        w, h = A4

        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(w / 2, h - 50, "ACADEMIA GALENO")

        c.setFont("Helvetica", 14)
        c.drawCentredString(w / 2, h - 80, "Reporte de Inventario")

        c.setFont("Helvetica", 10)
        c.drawString(50, h - 110, f"Fecha: {fecha}")

        y = h - 150
        c.setFont("Helvetica-Bold", 11)
        c.drawString(50, y, "Código")
        c.drawString(150, y, "Producto")
        c.drawString(360, y, "Stock")
        c.drawString(430, y, "Precio")

        y -= 20
        c.setFont("Helvetica", 10)

        for p in productos:
            c.drawString(50, y, p.get_codigo())
            c.drawString(150, y, p.get_nombre())
            c.drawString(370, y, str(p.get_stock()))
            c.drawString(430, y, f"S/ {p.get_precio():.2f}")
            y -= 18

            if y < 50:
                c.showPage()
                y = h - 50

        c.save()
        os.startfile(archivo)

        messagebox.showinfo("🖨️", "Reporte generado. ¡Listo para imprimir!")

# ===============================
# EJECUCIÓN
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioGalenoKids(root)
    root.mainloop()
