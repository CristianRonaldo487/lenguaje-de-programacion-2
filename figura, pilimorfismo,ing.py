import tkinter as tk
from tkinter import ttk, messagebox
import math

# ---------------------------
# Clases de figuras (Polimorfismo)
# ---------------------------
class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado**2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio**2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


# ---------------------------
# Interfaz gráfica con Tkinter
# ---------------------------
class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Áreas con Figuras")
        self.root.geometry("520x650")
        self.root.configure(bg="#1e1e1e")

        # Título
        tk.Label(root, text="🧮 Calculadora de Áreas", font=("Arial", 18, "bold"), fg="white", bg="#1e1e1e").pack(pady=10)

        # Selección de figura
        tk.Label(root, text="Selecciona una figura:", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack()
        self.combo = ttk.Combobox(root, values=["Cuadrado", "Círculo", "Triángulo"], state="readonly", font=("Arial", 12))
        self.combo.pack(pady=10)
        self.combo.bind("<<ComboboxSelected>>", self.mostrar_campos)

        # Frame para los campos de entrada
        self.frame_inputs = tk.Frame(root, bg="#1e1e1e")
        self.frame_inputs.pack(pady=10)

        # Botón para calcular
        tk.Button(root, text="Calcular Área y Dibujar", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", 
                  command=self.calcular_area).pack(pady=10)

        # Resultados
        self.resultado = tk.Label(root, text="", font=("Arial", 13, "bold"), fg="yellow", bg="#1e1e1e", justify="left")
        self.resultado.pack(pady=10)

        # Canvas para dibujar figuras
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)

    def mostrar_campos(self, event):
        # Limpia los campos anteriores
        for widget in self.frame_inputs.winfo_children():
            widget.destroy()

        figura = self.combo.get()

        if figura == "Cuadrado":
            tk.Label(self.frame_inputs, text="Lado:", fg="white", bg="#1e1e1e").grid(row=0, column=0, padx=5, pady=5)
            self.lado_entry = tk.Entry(self.frame_inputs)
            self.lado_entry.grid(row=0, column=1, padx=5, pady=5)

        elif figura == "Círculo":
            tk.Label(self.frame_inputs, text="Radio:", fg="white", bg="#1e1e1e").grid(row=0, column=0, padx=5, pady=5)
            self.radio_entry = tk.Entry(self.frame_inputs)
            self.radio_entry.grid(row=0, column=1, padx=5, pady=5)

        elif figura == "Triángulo":
            tk.Label(self.frame_inputs, text="Base:", fg="white", bg="#1e1e1e").grid(row=0, column=0, padx=5, pady=5)
            self.base_entry = tk.Entry(self.frame_inputs)
            self.base_entry.grid(row=0, column=1, padx=5, pady=5)
            tk.Label(self.frame_inputs, text="Altura:", fg="white", bg="#1e1e1e").grid(row=1, column=0, padx=5, pady=5)
            self.altura_entry = tk.Entry(self.frame_inputs)
            self.altura_entry.grid(row=1, column=1, padx=5, pady=5)

    def calcular_area(self):
        figura = self.combo.get()
        self.canvas.delete("all")  # Limpia el canvas

        try:
            if figura == "Cuadrado":
                lado = float(self.lado_entry.get())
                figura_obj = Cuadrado(lado)
                resultado = figura_obj.area()
                self.dibujar_cuadrado(lado)
                texto = f"📐 Figura: Cuadrado\n➡️ Lado: {lado}\n🟨 Área: {resultado:.2f}"

            elif figura == "Círculo":
                radio = float(self.radio_entry.get())
                figura_obj = Circulo(radio)
                resultado = figura_obj.area()
                self.dibujar_circulo(radio)
                texto = f"⚪ Figura: Círculo\n➡️ Radio: {radio}\n🟡 Área: {resultado:.2f}"

            elif figura == "Triángulo":
                base = float(self.base_entry.get())
                altura = float(self.altura_entry.get())
                figura_obj = Triangulo(base, altura)
                resultado = figura_obj.area()
                self.dibujar_triangulo(base, altura)
                texto = f"🔺 Figura: Triángulo\n➡️ Base: {base}\n➡️ Altura: {altura}\n🟥 Área: {resultado:.2f}"

            else:
                messagebox.showwarning("Advertencia", "Selecciona una figura primero.")
                return

            self.resultado.config(text=texto)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

    # ---------------------------
    # Métodos para dibujar figuras
    # ---------------------------
    def dibujar_cuadrado(self, lado):
        escala = 5  # Ajusta tamaño visual
        lado_escalado = lado * escala
        x0, y0 = 150 - lado_escalado / 2, 150 - lado_escalado / 2
        x1, y1 = 150 + lado_escalado / 2, 150 + lado_escalado / 2
        self.canvas.create_rectangle(x0, y0, x1, y1, outline="blue", width=3, fill="#87CEEB")

    def dibujar_circulo(self, radio):
        escala = 5
        radio_escalado = radio * escala
        x0, y0 = 150 - radio_escalado, 150 - radio_escalado
        x1, y1 = 150 + radio_escalado, 150 + radio_escalado
        self.canvas.create_oval(x0, y0, x1, y1, outline="red", width=3, fill="#FFB6C1")

    def dibujar_triangulo(self, base, altura):
        escala = 5
        base_escalada = base * escala
        altura_escalada = altura * escala
        x_centro = 150
        y_base = 260
        self.canvas.create_polygon(
            x_centro - base_escalada / 2, y_base,
            x_centro + base_escalada / 2, y_base,
            x_centro, y_base - altura_escalada,
            outline="green", fill="#90EE90", width=3
        )


# ---------------------------
# Ejecutar la aplicación
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
