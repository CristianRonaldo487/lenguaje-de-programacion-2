import tkinter as tk
import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera, salida):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.salida = salida
        self.salida.insert(tk.END, f"Estudiante registrado {self.nombre}. {self.edad} años, {self.carrera}\n")

    def mostrar_informacion(self):
        self.salida.insert(tk.END, f"{self.nombre} tiene {self.edad} años y estudia {self.carrera}\n")

    def __del__(self):
        self.salida.insert(tk.END, f"Estudiante eliminado {self.nombre}\n")


grupo = []

def agregar_estudiante():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    carrera = entry_carrera.get()

    if nombre and edad and carrera:
        try:
            edad = int(edad)
        except ValueError:
            salida.insert(tk.END, "⚠️ La edad debe ser un número.\n")
            return

        estudiante = Estudiante(nombre, edad, carrera, salida)
        grupo.append(estudiante)

        # limpiar entradas
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_carrera.delete(0, tk.END)
    else:
        salida.insert(tk.END, "⚠️ Debe completar todos los campos.\n")


def mostrar_estudiantes():
    if grupo:
        for estudiante in grupo:
            estudiante.mostrar_informacion()
    else:
        salida.insert(tk.END, "⚠️ No hay estudiantes registrados.\n")


def eliminar_estudiantes():
    grupo.clear()
    gc.collect()
    salida.insert(tk.END, "Todos los estudiantes eliminados.\n")


# Interfaz Tkinter
root = tk.Tk()
root.title("Gestión de Estudiantes")
root.geometry("500x500")

# Entradas de datos
tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root, width=40)
entry_nombre.pack()

tk.Label(root, text="Edad:").pack()
entry_edad = tk.Entry(root, width=40)
entry_edad.pack()

tk.Label(root, text="Carrera:").pack()
entry_carrera = tk.Entry(root, width=40)
entry_carrera.pack()

# Botones
btn_agregar = tk.Button(root, text="Agregar Estudiante", command=agregar_estudiante)
btn_agregar.pack(pady=5)

btn_mostrar = tk.Button(root, text="Mostrar Estudiantes", command=mostrar_estudiantes)
btn_mostrar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Estudiantes", command=eliminar_estudiantes)
btn_eliminar.pack(pady=5)

# Área de salida
salida = tk.Text(root, height=15, width=60)
salida.pack(pady=10)

root.mainloop()








    


            