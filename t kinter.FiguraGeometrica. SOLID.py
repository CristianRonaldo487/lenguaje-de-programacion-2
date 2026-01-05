import tkinter as tk
import math


# ====== MODELO (Lógica) ======

class FiguraGeometrica:
    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# ====== VISTA + CONTROLADOR (Tkinter) ======

class AppFiguras(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎨 Figuras Geométricas para Niños")
        self.geometry("420x420")
        self.config(bg="#E8F6FF")

        self.figura = tk.StringVar(value="Circulo")

        # Título
        tk.Label(
            self,
            text="📐 JUGUEMOS CON FIGURAS 📐",
            font=("Comic Sans MS", 16, "bold"),
            bg="#E8F6FF",
            fg="#1A5276"
        ).pack(pady=10)

        # Selección de figura
        frame_opcion = tk.Frame(self, bg="#E8F6FF")
        frame_opcion.pack()

        tk.Radiobutton(
            frame_opcion, text="🔵 Círculo",
            variable=self.figura, value="Circulo",
            font=("Comic Sans MS", 11),
            bg="#E8F6FF",
            command=self.actualizar_campos
        ).grid(row=0, column=0, padx=10)

        tk.Radiobutton(
            frame_opcion, text="🟩 Rectángulo",
            variable=self.figura, value="Rectangulo",
            font=("Comic Sans MS", 11),
            bg="#E8F6FF",
            command=self.actualizar_campos
        ).grid(row=0, column=1, padx=10)

        # Entradas
        self.frame_datos = tk.Frame(self, bg="#E8F6FF")
        self.frame_datos.pack(pady=15)

        self.label1 = tk.Label(
            self.frame_datos, text="Radio:",
            font=("Comic Sans MS", 11),
            bg="#E8F6FF"
        )
        self.entry1 = tk.Entry(self.frame_datos, font=("Comic Sans MS", 11))

        self.label2 = tk.Label(
            self.frame_datos, text="Altura:",
            font=("Comic Sans MS", 11),
            bg="#E8F6FF"
        )
        self.entry2 = tk.Entry(self.frame_datos, font=("Comic Sans MS", 11))

        self.label1.grid(row=0, column=0, pady=5)
        self.entry1.grid(row=0, column=1, pady=5)

        # Botón
        tk.Button(
            self,
            text="✨ CALCULAR ✨",
            font=("Comic Sans MS", 12, "bold"),
            bg="#58D68D",
            fg="white",
            width=18,
            command=self.calcular
        ).pack(pady=10)

        # Resultado
        self.resultado = tk.Label(
            self,
            text="😊 Aquí verás el resultado 😊",
            font=("Comic Sans MS", 12),
            bg="#FFF3CD",
            fg="#7D6608",
            width=35,
            height=4
        )
        self.resultado.pack(pady=10)

        self.actualizar_campos()

    def actualizar_campos(self):
        if self.figura.get() == "Circulo":
            self.label1.config(text="Radio:")
            self.label2.grid_forget()
            self.entry2.grid_forget()
        else:
            self.label1.config(text="Base:")
            self.label2.config(text="Altura:")
            self.label2.grid(row=1, column=0, pady=5)
            self.entry2.grid(row=1, column=1, pady=5)

    def calcular(self):
        try:
            if self.figura.get() == "Circulo":
                radio = float(self.entry1.get())
                figura = Circulo(radio)
                emoji = "🔵"
            else:
                base = float(self.entry1.get())
                altura = float(self.entry2.get())
                figura = Rectangulo(base, altura)
                emoji = "🟩"

            area = figura.area()
            perimetro = figura.perimetro()

            self.resultado.config(
                text=f"{emoji} Área: {area:.2f}\n{emoji} Perímetro: {perimetro:.2f}"
            )
        except ValueError:
            self.resultado.config(text="❌ Escribe números correctos")


# ====== Ejecutar ======
if __name__ == "__main__":
    app = AppFiguras()
    app.mainloop()
