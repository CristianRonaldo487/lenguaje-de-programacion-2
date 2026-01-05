import tkinter as tk
from tkinter import messagebox

class TablaMultiplicar:
    def __init__(self, numero):
        self.numero = numero

    def generartabla(self):
        tabla = []
        for i in range(1, 11):
            resultado = self.numero * i
            tabla.append(f"{self.numero} x {i} = {resultado}")
        return tabla

def generar_tabla():
    try:
        numero = int(entry_numero.get())
        miTabla = TablaMultiplicar(numero)
        resultado = miTabla.generartabla()

        # Mostrar en el label
        texto_tabla = "\n".join(resultado)
        label_resultado.config(text=texto_tabla)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Tabla de Multiplicar")
ventana.geometry("350x400")
ventana.configure(bg="lightblue")  # Fondo celeste

label_instruccion = tk.Label(ventana, text="Ingrese un número:", font=("Arial", 12), bg="lightblue")
label_instruccion.pack(pady=5)

entry_numero = tk.Entry(ventana, font=("Arial", 12))
entry_numero.pack(pady=5)

btn_generar = tk.Button(ventana, text="Generar Tabla", font=("Arial", 12), command=generar_tabla)
btn_generar.pack(pady=10)

label_resultado = tk.Label(ventana, text="", font=("Courier", 12), fg="darkgreen", bg="lightblue", justify="left")
label_resultado.pack(pady=10)

ventana.mainloop()
