import tkinter as tk
from tkinter import ttk, messagebox

# === CLASES BASE ===
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"👋 Hola, soy {self.nombre} y tengo {self.edad} años."

class Trabajador:
    def __init__(self, profesion, salario):
        self.profesion = profesion
        self.salario = salario

    def trabajar(self):
        return f"💼 Trabajo como {self.profesion} y gano ${self.salario:,}."

class Estudiante:
    def __init__(self, carrera, universidad):
        self.carrera = carrera
        self.universidad = universidad

    def estudiar(self):
        return f"🎓 Estudio {self.carrera} en la Universidad {self.universidad}."

# === HERENCIA MÚLTIPLE ===
class PersonaMultirol(Persona, Trabajador, Estudiante):
    def __init__(self, nombre, edad, profesion, salario, carrera, universidad):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, profesion, salario)
        Estudiante.__init__(self, carrera, universidad)

    def mostrar_informacion(self):
        info = (
            "===== PERFIL COMPLETO =====\n"
            f"{self.presentarse()}\n\n"
            f"{self.trabajar()}\n\n"
            f"{self.estudiar()}\n\n"
            f"🌟 {self.nombre} es una persona dedicada, apasionada y con un gran futuro por delante."
        )
        return info

# === FUNCIONALIDAD DE LA INTERFAZ ===
def mostrar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    profesion = entry_profesion.get()
    salario = entry_salario.get()
    carrera = entry_carrera.get()
    universidad = entry_universidad.get()

    # Validación
    if not all([nombre, edad, profesion, salario, carrera, universidad]):
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos antes de continuar.")
        return

    try:
        edad = int(edad)
        salario = float(salario)
    except ValueError:
        messagebox.showerror("Error de formato", "Edad y salario deben ser números.")
        return

    persona = PersonaMultirol(nombre, edad, profesion, salario, carrera, universidad)
    resultado = persona.mostrar_informacion()

    texto_resultado.config(state="normal")
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, resultado)
    texto_resultado.config(state="disabled")

# === INTERFAZ GRÁFICA ===
ventana = tk.Tk()
ventana.title("💚 Herencia Múltiple - Persona Multirol 💚")
ventana.geometry("550x650")
ventana.config(bg="#ccffcc")
ventana.resizable(False, False)

# === TÍTULO ===
titulo = tk.Label(
    ventana,
    text="Registro de Persona Multirol",
    bg="#ccffcc",
    fg="#004d00",
    font=("Arial Rounded MT Bold", 20)
)
titulo.pack(pady=10)

# === MARCO PARA CAMPOS ===
marco = tk.Frame(ventana, bg="white", bd=2, relief="ridge")
marco.pack(pady=10, padx=15, fill="both", expand=False)

# === FUNCIÓN PARA CREAR CAMPOS ===
def crear_campo(texto):
    tk.Label(marco, text=texto, bg="white", fg="#004d00", font=("Arial", 10, "bold")).pack(pady=4)
    entry = tk.Entry(marco, justify="center", bd=1, relief="solid", width=35)
    entry.pack(pady=3, ipady=4)
    return entry

entry_nombre = crear_campo("Nombre:")
entry_edad = crear_campo("Edad:")
entry_profesion = crear_campo("Profesión:")
entry_salario = crear_campo("Salario:")
entry_carrera = crear_campo("Carrera:")
entry_universidad = crear_campo("Universidad:")

# === BOTÓN ===
boton = ttk.Button(
    ventana,
    text="Mostrar Información",
    command=mostrar_datos
)
boton.pack(pady=20)

# === CUADRO DE RESULTADO (más grande y decorado) ===
frame_resultado = tk.Frame(ventana, bg="#b3ffb3", bd=3, relief="solid")
frame_resultado.pack(padx=20, pady=10, fill="both", expand=True)

texto_resultado = tk.Text(
    frame_resultado,
    height=12,
    width=60,
    font=("Consolas", 11),
    wrap="word",
    bg="#eaffea",
    fg="#003300",
    state="disabled",
    relief="flat"
)
texto_resultado.pack(padx=10, pady=10, fill="both", expand=True)

# ==
