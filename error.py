import tkinter as tk
from tkinter import messagebox
import math

def calcular_hipotenusa():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser positivos.")

        hipotenusa = math.sqrt(a**2 + b**2)
        resultado_label.config(text=f"La hipotenusa es: {hipotenusa:.2f}")

    except ValueError as ve:
        messagebox.showerror("Error", f"Entrada inválida: {ve}")
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Calculadora de Hipotenusa")
ventana.geometry("350x250")
ventana.resizable(False, False)
ventana.config(bg="#e6e6e6")

# --- Título ---
titulo = tk.Label(ventana, text="Cálculo de Hipotenusa", 
                  font=("Arial", 16, "bold"), bg="#e6e6e6")
titulo.pack(pady=10)

# --- Frame para entradas ---
frame = tk.Frame(ventana, bg="#e6e6e6")
frame.pack(pady=5)

# Entrada A
label_a = tk.Label(frame, text="Cateto A:", font=("Arial", 12), bg="#e6e6e6")
label_a.grid(row=0, column=0, padx=5, pady=5)

entry_a = tk.Entry(frame, font=("Arial", 12), width=10)
entry_a.grid(row=0, column=1, padx=5, pady=5)

# Entrada B
label_b = tk.Label(frame, text="Cateto B:", font=("Arial", 12), bg="#e6e6e6")
label_b.grid(row=1, column=0, padx=5, pady=5)

entry_b = tk.Entry(frame, font=("Arial", 12), width=10)
entry_b.grid(row=1, column=1, padx=5, pady=5)

# --- Botón calcular ---
btn = tk.Button(ventana, text="Calcular", font=("Arial", 12, "bold"),
                command=calcular_hipotenusa, bg="#4CAF50", fg="white",
                width=12, cursor="hand2")
btn.pack(pady=10)

# --- Resultado ---
resultado_label = tk.Label(ventana, text="", font=("Arial", 14, "bold"), 
                           bg="#e6e6e6", fg="#333")
resultado_label.pack(pady=10)

# Iniciar ventana
ventana.mainloop()
