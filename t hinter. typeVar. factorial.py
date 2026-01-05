from typing import TypeVar, Generic
import tkinter as tk
from tkinter import messagebox

T = TypeVar('T', int, float)

class CalculadoraFactorial(Generic[T]):
    def __init__(self, numero: T):
        self.numero = numero

    def calcular_factorial(self) -> int:
        n = int(self.numero)

        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


def calcular():
    try:
        n = float(entry_numero.get())
        calc = CalculadoraFactorial(n)
        resultado = calc.calcular_factorial()
        resultado_label.config(text=f"Factorial = {resultado}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


# ======== VENTANA PRINCIPAL ========
ventana = tk.Tk()
ventana.title("Calculadora de Factorial")
ventana.geometry("380x260")
ventana.resizable(False, False)
ventana.config(bg="#f0f0f0")

# ======== TÍTULO ========
titulo = tk.Label(ventana, text="Calculadora de Factorial",
                  font=("Arial", 18, "bold"), bg="#f0f0f0")
titulo.pack(pady=15)

# ======== FRAME DE ENTRADA ========
frame = tk.Frame(ventana, bg="#f0f0f0")
frame.pack()

label_numero = tk.Label(frame, text="Ingrese un número:", font=("Arial", 12), bg="#f0f0f0")
label_numero.grid(row=0, column=0, padx=5, pady=10)

entry_numero = tk.Entry(frame, font=("Arial", 12), width=12)
entry_numero.grid(row=0, column=1, padx=5, pady=10)

# ======== BOTÓN ========
btn = tk.Button(ventana, text="Calcular", font=("Arial", 12, "bold"),
                bg="#4CAF50", fg="white", cursor="hand2",
                width=12, command=calcular)
btn.pack(pady=10)

# ======== RESULTADO ========
resultado_label = tk.Label(ventana, text="", font=("Arial", 14, "bold"),
                           bg="#f0f0f0")
resultado_label.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
