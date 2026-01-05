import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# ==============================
#  BASE DE DATOS
# ==============================
def crear_tabla():
    conn = sqlite3.connect("pagos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dni TEXT,
            nombre TEXT,
            destinatario TEXT,
            metodo_pago TEXT,
            monto REAL,
            fecha TEXT,
            hora TEXT,
            contraseña TEXT
        )
    """)
    conn.commit()
    conn.close()

crear_tabla()

# ==============================
#  CLASES DE PAGO
# ==============================
class MetodoPago:
    def pagar(self, monto):
        pass

class TarjetaCredito(MetodoPago):
    def pagar(self, monto):
        return f"Pago con Tarjeta de Crédito por S/.{monto:.2f}"

class PayPal(MetodoPago):
    def pagar(self, monto):
        return f"Pago con PayPal por S/.{monto:.2f}"

class Efectivo(MetodoPago):
    def pagar(self, monto):
        return f"Pago en Efectivo por S/.{monto:.2f}"

# ==============================
#  APLICACIÓN TKINTER
# ==============================
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Pago")
        self.root.geometry("500x550")
        self.root.config(bg="#f4f4f4")

        tk.Label(root, text="💳 SISTEMA DE PAGO", font=("Arial", 18, "bold"), bg="#f4f4f4", fg="#333").pack(pady=10)

        # Campos de entrada
        self.crear_campo("DNI:", 0)
        self.crear_campo("Nombre:", 1)
        self.crear_campo("Destinatario:", 2)
        self.crear_campo("Monto:", 3)

        # Método de pago
        tk.Label(root, text="Método de Pago:", bg="#f4f4f4", fg="#333", font=("Arial", 12)).pack(pady=5)
        self.metodo_pago = ttk.Combobox(root, values=["Tarjeta de Crédito", "PayPal", "Efectivo"], state="readonly", font=("Arial", 12))
        self.metodo_pago.pack(pady=5)

        # Contraseña
        tk.Label(root, text="Crea una Contraseña para el pago:", bg="#f4f4f4", fg="#333", font=("Arial", 12)).pack(pady=5)
        self.contraseña_entry = tk.Entry(root, show="*", font=("Arial", 12))
        self.contraseña_entry.pack(pady=5)

        # Botón de pago
        tk.Button(root, text="Realizar Pago", command=self.realizar_pago, bg="#0078D7", fg="white", font=("Arial", 12, "bold"), width=20).pack(pady=20)

    def crear_campo(self, texto, fila):
        frame = tk.Frame(self.root, bg="#f4f4f4")
        frame.pack(pady=5)
        tk.Label(frame, text=texto, bg="#f4f4f4", fg="#333", font=("Arial", 12)).pack(side="left", padx=5)
        entry = tk.Entry(frame, font=("Arial", 12))
        entry.pack(side="left", padx=5)
        setattr(self, f"entry_{fila}", entry)

    def realizar_pago(self):
        dni = self.entry_0.get()
        nombre = self.entry_1.get()
        destinatario = self.entry_2.get()
        monto = self.entry_3.get()
        metodo = self.metodo_pago.get()
        contraseña = self.contraseña_entry.get()

        if not (dni and nombre and destinatario and monto and metodo and contraseña):
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
            return

        try:
            monto = float(monto)
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número.")
            return

        # Polimorfismo
        if metodo == "Tarjeta de Crédito":
            pago = TarjetaCredito()
        elif metodo == "PayPal":
            pago = PayPal()
        else:
            pago = Efectivo()

        mensaje_pago = pago.pagar(monto)
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")

        # Guardar en base de datos
        conn = sqlite3.connect("pagos.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pagos (dni, nombre, destinatario, metodo_pago, monto, fecha, hora, contraseña)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (dni, nombre, destinatario, metodo, monto, fecha, hora, contraseña))
        conn.commit()
        conn.close()

        # Mostrar baucher
        self.mostrar_baucher(dni, nombre, destinatario, metodo, monto, fecha, hora, mensaje_pago)

    def mostrar_baucher(self, dni, nombre, destinatario, metodo, monto, fecha, hora, mensaje_pago):
        baucher = tk.Toplevel(self.root)
        baucher.title("🧾 Comprobante de Pago")
        baucher.geometry("400x450")
        baucher.config(bg="white")

        tk.Label(baucher, text="COMPROBANTE DE PAGO", font=("Arial", 16, "bold"), fg="#0078D7", bg="white").pack(pady=15)

        detalles = [
            f"DNI: {dni}",
            f"Nombre: {nombre}",
            f"Destinatario: {destinatario}",
            f"Método de Pago: {metodo}",
            f"Monto: S/. {monto:.2f}",
            f"Fecha: {fecha}",
            f"Hora: {hora}",
            "",
            f"{mensaje_pago}",
            "",
            "✅ Transacción realizada con éxito",
            "🔐 Contraseña registrada correctamente"
        ]

        for texto in detalles:
            tk.Label(baucher, text=texto, bg="white", fg="#333", font=("Arial", 12)).pack(pady=3)

        tk.Button(baucher, text="Cerrar", command=baucher.destroy, bg="#0078D7", fg="white", font=("Arial", 11, "bold"), width=15).pack(pady=20)


# ==============================
#  EJECUCIÓN
# ==============================
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

