import tkinter as tk
from tkinter import messagebox

def generar_fibonacci():
    try:
        n = int(entry_n.get())

        if n <= 0:
            raise ValueError("Debe ser un número entero positivo.")

        # Generar Fibonacci SIN LISTAS
        a, b = 0, 1
        resultado = ""

        for _ in range(n):
            resultado += str(a) + " "
            a, b = b, a + b

        resultado_label.config(text=resultado)

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))


# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Serie de Fibonacci")
ventana.geometry("420x300")
ventana.resizable(False, False)
ventana.configure(bg="#f2f2f2")

# --- Título ---
titulo = tk.Label(ventana, text="Generador de Fibonacci",
                  font=("Arial", 18, "bold"), bg="#f2f2f2")
titulo.pack(pady=15)

# --- Frame entradas ---
frame = tk.Frame(ventana, bg="#f2f2f2")
frame.pack()

label_n = tk.Label(frame, text="Cantidad de términos:", font=("Arial", 12), bg="#f2f2f2")
label_n.grid(row=0, column=0, padx=5, pady=10)

entry_n = tk.Entry(frame, font=("Arial", 12), width=10)
entry_n.grid(row=0, column=1, padx=5, pady=10)

# --- Botón ---
btn = tk.Button(ventana, text="Generar",
                font=("Arial", 12, "bold"),
                bg="#4CAF50", fg="white", cursor="hand2",
                command=generar_fibonacci, width=12)
btn.pack(pady=10)

# --- Resultado ---
resultado_label = tk.Label(ventana, text="", font=("Arial", 12),
                           bg="#f2f2f2", wraplength=380, justify="center")
resultado_label.pack(pady=15)

ventana.mainloop()
