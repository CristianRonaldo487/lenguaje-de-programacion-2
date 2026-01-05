import tkinter as tk
from tkinter import messagebox

class SignoZodiacal:
    def __init__(self, dia, mes):
        self.dia = dia
        self.mes = mes

    def mostrar_signo(self):
        dia = self.dia
        mes = self.mes

        if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
            return "Aries"
        elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
            return "Tauro"
        elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
            return "Géminis"
        elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
            return "Cáncer"
        elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
            return "Leo"
        elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
            return "Virgo"
        elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 23):
            return "Libra"
        elif (mes == 10 and dia >= 24) or (mes == 11 and dia <= 22):
            return "Escorpio"
        elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
            return "Sagitario"
        elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
            return "Capricornio"
        elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
            return "Acuario"
        elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
            return "Piscis"
        else:
            return "Fecha inválida"

# Función para el botón
def calcular_signo():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        persona = SignoZodiacal(dia, mes)
        signo = persona.mostrar_signo()
        messagebox.showinfo("Resultado", f"Tu signo zodiacal es: {signo}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Signo Zodiacal")
ventana.geometry("300x200")

# Etiquetas y entradas
tk.Label(ventana, text="Día de nacimiento (1-31):").pack(pady=5)
entry_dia = tk.Entry(ventana)
entry_dia.pack()

tk.Label(ventana, text="Mes de nacimiento (1-12):").pack(pady=5)
entry_mes = tk.Entry(ventana)
entry_mes.pack()

# Botón
btn_calcular = tk.Button(ventana, text="Mostrar Signo", command=calcular_signo)
btn_calcular.pack(pady=10)

# Iniciar ventana
ventana.mainloop()
