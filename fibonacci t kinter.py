import tkinter as tk
from tkinter import messagebox

class Fibonacci:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.serie = []

    def generarserie(self):
        a, b = 0, 1
        for _ in range(self.cantidad):
            self.serie.append(a)
            a, b = b, a + b
        return self.serie

def generar_fibonacci():
    try:
        cantidad = int(entry_cantidad.get())
        if cantidad <= 0:
            messagebox.showerror("Error", "Ingrese un número mayor que 0.")
            return

        miFibonacci = Fibonacci(cantidad)
        resultado = miFibonacci.generarserie()
        label_resultado.config(text=f"Serie Fibonacci ({cantidad} términos):\n{resultado}")

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Serie de Fibonacci")
ventana.geometry("400x250")

label_instruccion = tk.Label(ventana, text="Ingrese la cantidad de términos:", font=("Arial", 12))
label_instruccion.pack(pady=5)

entry_cantidad = tk.Entry(ventana, font=("Arial", 12))
entry_cantidad.pack(pady=5)

btn_generar = tk.Button(ventana, text="Generar Serie", font=("Arial", 12), command=generar_fibonacci)
btn_generar.pack(pady=10)

label_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue", wraplength=350, justify="left")
label_resultado.pack(pady=10)

ventana.mainloop()
