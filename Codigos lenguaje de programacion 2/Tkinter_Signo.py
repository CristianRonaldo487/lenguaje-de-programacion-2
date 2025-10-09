import tkinter as tk
from tkinter import messagebox

class Persona:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes
        self.signo = self.obtener_signo()

    def obtener_signo(self):
        if (self.mes == 3 and self.dia >= 21) or (self.mes == 4 and self.dia <= 19):
            return "Aries"
        elif (self.mes == 4 and self.dia >= 20) or (self.mes == 5 and self.dia <= 20):
            return "Tauro"
        elif (self.mes == 5 and self.dia >= 21) or (self.mes == 6 and self.dia <= 20):
            return "Géminis"
        elif (self.mes == 6 and self.dia >= 21) or (self.mes == 7 and self.dia <= 22):
            return "Cáncer"
        elif (self.mes == 7 and self.dia >= 23) or (self.mes == 8 and self.dia <= 22):
            return "Leo"
        elif (self.mes == 8 and self.dia >= 23) or (self.mes == 9 and self.dia <= 22):
            return "Virgo"
        elif (self.mes == 9 and self.dia >= 23) or (self.mes == 10 and self.dia <= 22):
            return "Libra"
        elif (self.mes == 10 and self.dia >= 23) or (self.mes == 11 and self.dia <= 21):
            return "Escorpio"
        elif (self.mes == 11 and self.dia >= 22) or (self.mes == 12 and self.dia <= 21):
            return "Sagitario"
        elif (self.mes == 12 and self.dia >= 22) or (self.mes == 1 and self.dia <= 19):
            return "Capricornio"
        elif (self.mes == 1 and self.dia >= 20) or (self.mes == 2 and self.dia <= 18):
            return "Acuario"
        elif (self.mes == 2 and self.dia >= 19) or (self.mes == 3 and self.dia <= 20):
            return "Piscis"
        else:
            return "Fecha inválida"

def calcular_signo():
    try:
        nombre = entry_nombre.get()
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())

        persona = Persona(nombre, dia, mes)
        messagebox.showinfo("Resultado", f"Hola {persona.nombre}, naciste el {persona.dia}/{persona.mes} "
                                         f"y tu signo es {persona.signo}.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores válidos.")

# -------- Ventana principal --------
ventana = tk.Tk()
ventana.title("Calculadora de Signo Zodiacal")

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

tk.Label(ventana, text="Día de nacimiento:").grid(row=1, column=0, padx=10, pady=5)
entry_dia = tk.Entry(ventana)
entry_dia.grid(row=1, column=1, padx=10, pady=5)

tk.Label(ventana, text="Mes de nacimiento:").grid(row=2, column=0, padx=10, pady=5)
entry_mes = tk.Entry(ventana)
entry_mes.grid(row=2, column=1, padx=10, pady=5)

# Botón
btn_calcular = tk.Button(ventana, text="Calcular Signo", command=calcular_signo)
btn_calcular.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()
