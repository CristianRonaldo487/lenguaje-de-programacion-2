from typing import TypeVar, Generic
import tkinter as tk
from tkinter import messagebox
import math

T = TypeVar("T", int, float)

# ===================================================
#  CLASE GENÉRICA BASE
# ===================================================
class FiguraGeometrica(Generic[T]):
    def area(self) -> T:
        raise NotImplementedError

    def perimetro(self) -> T:
        raise NotImplementedError

# ===================================================
#  RECTÁNGULO
# ===================================================
class Rectangulo(FiguraGeometrica[T]):
    def __init__(self, base: T, altura: T):
        self.base = base
        self.altura = altura

    def area(self) -> T:
        return self.base * self.altura

    def perimetro(self) -> T:
        return 2 * (self.base + self.altura)

# ===================================================
#  CÍRCULO
# ===================================================
class Circulo(FiguraGeometrica[T]):
    def __init__(self, radio: T):
        self.radio = radio

    def area(self) -> T:
        return math.pi * self.radio**2

    def perimetro(self) -> T:
        return 2 * math.pi * self.radio

# ===================================================
#  INTERFAZ TKINTER
# ===================================================
ventana = tk.Tk()
ventana.title("Figuras con Representación en Recta 🎨")
ventana.geometry("750x520")
ventana.config(bg="#B2F0FF")

# Canvas donde se dibuja la figura
canvas_fig = tk.Canvas(ventana, width=300, height=260, bg="white", bd=4, relief="ridge")
canvas_fig.place(x=420, y=20)

# Canvas donde se dibujan las rectas de área y perímetro
canvas_rectas = tk.Canvas(ventana, width=300, height=200, bg="#FFFCE0", bd=4, relief="ridge")
canvas_rectas.place(x=420, y=300)

# -------------------------------------------------------------
# Funciones para mostrar rectas de área y perímetro
# -------------------------------------------------------------
def dibujar_rectas(area, perimetro):
    canvas_rectas.delete("all")
    
    # Escala visual (para que no se salga del canvas)
    escala = 3

    area_visual = area / escala
    per_visual = perimetro / escala

    # Área (recta roja)
    canvas_rectas.create_line(20, 60, 20 + area_visual, 60, width=12, fill="red")
    canvas_rectas.create_text(20, 40, text=f"Área: {area:.2f}", font=("Comic Sans MS", 14), anchor="w", fill="red")

    # Perímetro (recta azul)
    canvas_rectas.create_line(20, 150, 20 + per_visual, 150, width=12, fill="blue")
    canvas_rectas.create_text(20, 130, text=f"Perímetro: {perimetro:.2f}", font=("Comic Sans MS", 14), anchor="w", fill="blue")

# -------------------------------------------------------------
# Mostrar rectángulo
# -------------------------------------------------------------
def mostrar_rectangulo():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())

        rect = Rectangulo(base, altura)

        area = rect.area()
        per = rect.perimetro()

        canvas_fig.delete("all")

        # Dibujar rectángulo centrado
        x1, y1 = 50, 50
        x2, y2 = x1 + base, y1 + altura

        canvas_fig.create_rectangle(x1, y1, x2, y2, fill="#FF9999", outline="black", width=4)

        # Dibujar rectas de representación
        dibujar_rectas(area, per)

    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos.")

# -------------------------------------------------------------
# Mostrar círculo
# -------------------------------------------------------------
def mostrar_circulo():
    try:
        radio = float(entry_radio.get())

        circ = Circulo(radio)

        area = circ.area()
        per = circ.perimetro()

        canvas_fig.delete("all")

        # Dibujar círculo
        canvas_fig.create_oval(
            150 - radio, 130 - radio,
            150 + radio, 130 + radio,
            fill="#99FF99", outline="black", width=4
        )

        # Dibujar rectas de representación
        dibujar_rectas(area, per)

    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido.")

# ===================================================
# ELEMENTOS IZQUIERDA
# ===================================================
titulo = tk.Label(ventana, text="FIGURAS GEOMÉTRICAS", font=("Comic Sans MS", 24, "bold"),
                  bg="#B2F0FF", fg="#FF4D4D")
titulo.place(x=40, y=10)

# RECTÁNGULO
tk.Label(ventana, text="Base del rectángulo:", bg="#B2F0FF", font=("Comic Sans MS", 14)).place(x=30, y=70)
entry_base = tk.Entry(ventana, font=("Comic Sans MS", 14), width=8)
entry_base.place(x=220, y=70)

tk.Label(ventana, text="Altura:", bg="#B2F0FF", font=("Comic Sans MS", 14)).place(x=30, y=110)
entry_altura = tk.Entry(ventana, font=("Comic Sans MS", 14), width=8)
entry_altura.place(x=220, y=110)

btn_rect = tk.Button(ventana, text="Mostrar Rectángulo 🟥", command=mostrar_rectangulo,
                     bg="#FF6F61", fg="white", font=("Comic Sans MS", 14, "bold"))
btn_rect.place(x=80, y=150)

# CÍRCULO
tk.Label(ventana, text="Radio del círculo:", bg="#B2F0FF", font=("Comic Sans MS", 14)).place(x=30, y=220)
entry_radio = tk.Entry(ventana, font=("Comic Sans MS", 14), width=8)
entry_radio.place(x=220, y=220)

btn_circ = tk.Button(ventana, text="Mostrar Círculo 🟢", command=mostrar_circulo,
                     bg="#34C759", fg="white", font=("Comic Sans MS", 14, "bold"))
btn_circ.place(x=80, y=260)

ventana.mainloop()
