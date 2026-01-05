from typing import TypeVar, Generic
import tkinter as tk
from tkinter import ttk, messagebox

T = TypeVar("T", int, float)

class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):
        self.a = a
        self.b = b

    def sumar(self) -> T:
        return self.a + self.b

    def restar(self) -> T:
        return self.a - self.b

    def multiplicar(self) -> T:
        return self.a * self.b

    def dividir(self) -> T:
        if self.b == 0:
            raise ValueError("❌ No se puede dividir entre cero")
        return self.a / self.b


def crear_interfaz():

    root = tk.Tk()
    root.title("Calculadora Divertida 🎉")
    root.geometry("500x550")
    root.configure(bg="#ffefd5")  # pastel peach

    # =================== TÍTULO ===================
    titulo = tk.Label(
        root,
        text="✨ CALCULADORA DIVERTIDA ✨",
        font=("Comic Sans MS", 24, "bold"),
        bg="#ffefd5",
        fg="#ff1493"
    )
    titulo.pack(pady=20)

    # =================== MARCO PRINCIPAL ===================
    frame = tk.Frame(root, bg="#ffefd5")
    frame.pack()

    # Etiquetas e Inputs
    lbl_a = tk.Label(frame, text="🔵 Número A:", font=("Comic Sans MS", 18),
                     bg="#ffefd5", fg="#1e90ff")
    lbl_a.grid(row=0, column=0, padx=10, pady=10)
    entry_a = tk.Entry(frame, font=("Comic Sans MS", 18), width=8,
                       bg="#e0ffff", fg="black")
    entry_a.grid(row=0, column=1)

    lbl_b = tk.Label(frame, text="🟢 Número B:", font=("Comic Sans MS", 18),
                     bg="#ffefd5", fg="#32cd32")
    lbl_b.grid(row=1, column=0, padx=10, pady=10)
    entry_b = tk.Entry(frame, font=("Comic Sans MS", 18), width=8,
                       bg="#f0fff0", fg="black")
    entry_b.grid(row=1, column=1)

    # =================== TIPO DE DATO ===================
    lbl_tipo = tk.Label(root, text="🔤 Tipo de dato:",
                        font=("Comic Sans MS", 18),
                        bg="#ffefd5", fg="#ff8c00")
    lbl_tipo.pack(pady=10)

    combo = ttk.Combobox(root, values=["int", "float"], state="readonly",
                         font=("Comic Sans MS", 16), width=8)
    combo.set("int")
    combo.pack()

    # =================== RESULTADO ===================
    lbl_result_title = tk.Label(
        root, text="📘 Resultado:",
        font=("Comic Sans MS", 22, "bold"),
        bg="#ffefd5", fg="#00008b"
    )
    lbl_result_title.pack(pady=15)

    resultado = tk.Label(
        root, text="",
        font=("Comic Sans MS", 40, "bold"),
        bg="#ffffe0", fg="#00008b",
        width=8, height=1
    )
    resultado.pack(pady=10)

    # =================== FUNCIÓN OPERAR ===================
    def operar(op):
        try:
            a = entry_a.get()
            b = entry_b.get()

            if combo.get() == "int":
                a = int(a)
                b = int(b)
                calc = Calculadora[int](a, b)
            else:
                a = float(a)
                b = float(b)
                calc = Calculadora[float](a, b)

            if op == "+":
                r = calc.sumar()
            elif op == "-":
                r = calc.restar()
            elif op == "*":
                r = calc.multiplicar()
            elif op == "/":
                r = calc.dividir()

            resultado.config(text=str(r))

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # =================== BOTONES ===================
    botones = tk.Frame(root, bg="#ffefd5")
    botones.pack(pady=30)

    btn_suma = tk.Button(
        botones, text="➕ SUMAR", font=("Comic Sans MS", 16, "bold"),
        bg="#87cefa", fg="black", width=10, command=lambda: operar("+")
    )
    btn_suma.grid(row=0, column=0, padx=10, pady=10)

    btn_restar = tk.Button(
        botones, text="➖ RESTAR", font=("Comic Sans MS", 16, "bold"),
        bg="#ffa07a", fg="black", width=10, command=lambda: operar("-")
    )
    btn_restar.grid(row=0, column=1, padx=10, pady=10)

    btn_multi = tk.Button(
        botones, text="✖ MULTIPLICAR", font=("Comic Sans MS", 16, "bold"),
        bg="#98fb98", fg="black", width=12, command=lambda: operar("*")
    )
    btn_multi.grid(row=1, column=0, padx=10, pady=10)

    btn_div = tk.Button(
        botones, text="➗ DIVIDIR", font=("Comic Sans MS", 16, "bold"),
        bg="#ffeb3b", fg="black", width=10, command=lambda: operar("/")
    )
    btn_div.grid(row=1, column=1, padx=10, pady=10)

    root.mainloop()


crear_interfaz()
