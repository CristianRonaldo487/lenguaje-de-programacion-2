import tkinter as tk
from tkinter import ttk, messagebox

def analizar_expresion(expresion: str) -> dict:
    """
    Analiza una expresión matemática en forma de string.
    Retorna un diccionario con:
    - variables encontradas
    - número de variables
    - número de operaciones
    """
    variables = set()
    operaciones = 0

    for i, c in enumerate(expresion):
        # Detectar variables (letras)
        if c.isalpha():
            variables.add(c)

        elif c in "+-*/^":
            operaciones += 1

        # Detectar multiplicación implícita
        if i < len(expresion) - 1:
            siguiente = expresion[i+1]
            if c.isdigit() and siguiente.isalpha():   # Ejemplo: 2x
                operaciones += 1
            elif c.isalpha() and siguiente.isalpha(): # Ejemplo: xy
                operaciones += 1

    return {
        "variables": sorted(variables),
        "num_variables": len(variables),
        "num_operaciones": operaciones
    }

def analizar():
    expresion = entrada.get().strip()

    if not expresion:
        messagebox.showwarning("Error", "Por favor ingrese una función matemática.")
        return

    analisis = analizar_expresion(expresion)

    resultado.set(
        f"Variables encontradas: {analisis['variables']}\n"
        f"Número de variables: {analisis['num_variables']}\n"
        f"Número de operaciones: {analisis['num_operaciones']}"
    )

# ----------------- INTERFAZ -----------------
ventana = tk.Tk()
ventana.title("Analizador de Funciones Matemáticas")
ventana.geometry("400x300")
ventana.configure(bg="#f4f6f7")

# Título
titulo = tk.Label(
    ventana, text="Analizador de Funciones", 
    font=("Arial", 16, "bold"), bg="#f4f6f7", fg="#2c3e50"
)
titulo.pack(pady=10)

# Entrada
entrada = ttk.Entry(ventana, font=("Consolas", 14))
entrada.pack(pady=10, ipadx=20, ipady=5)

# Botón
btn = ttk.Button(ventana, text="Analizar", command=analizar)
btn.pack(pady=10)

# Área de resultado
resultado = tk.StringVar()
label_resultado = tk.Label(
    ventana, textvariable=resultado, 
    font=("Consolas", 12), bg="#ecf0f1", fg="#2c3e50", 
    relief="groove", justify="left", anchor="w"
)
label_resultado.pack(fill="both", expand=True, padx=20, pady=10)

# Iniciar app
ventana.mainloop()
