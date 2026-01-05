import tkinter as tk
from tkinter import messagebox

class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dividir(self):
        try:
            resultado = self.a / self.b
            return f"Resultado: {resultado}"
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero."
        except Exception as e:
            return f"Ocurrió un error: {e}"
        finally:
            print("Operación finalizada")

# --- Función que se ejecuta al presionar el botón ---
def realizar_division():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operacion = Division(a, b)
        resultado = operacion.dividir()
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese solo números.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# --- Interfaz con Tkinter ---
ventana = tk.Tk()
ventana.title("División con Try-Except")
ventana.geometry("300x200")
ventana.config(bg="#1e1e1e")

# Etiquetas y entradas
tk.Label(ventana, text="Ingrese el valor de a:", fg="white", bg="#1e1e1e").pack(pady=5)
entry_a = tk.Entry(ventana, justify="center")
entry_a.pack()

tk.Label(ventana, text="Ingrese el valor de b:", fg="white", bg="#1e1e1e").pack(pady=5)
entry_b = tk.Entry(ventana, justify="center")
entry_b.pack()

# Botón para dividir
tk.Button(ventana, text="Dividir", command=realizar_division, bg="#007acc", fg="white").pack(pady=10)

# Iniciar la ventana
ventana.mainloop()
