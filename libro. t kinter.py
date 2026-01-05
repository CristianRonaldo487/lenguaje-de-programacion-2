import tkinter as tk
import gc

class Libro:
    def __init__(self, titulo, autor, anio, salida):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.salida = salida
        self.salida.insert(tk.END, f"Libro registrado: {self.titulo} de {self.autor}, {self.anio}\n")

    def mostrar_informacion(self):
        self.salida.insert(tk.END, f"'{self.titulo}' fue escrito por {self.autor} en {self.anio}\n")

    def __del__(self):
        self.salida.insert(tk.END, f"Libro eliminado: {self.titulo}\n")


# Lista de libros
biblioteca = []

def agregar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()

    if titulo and autor and anio:
        try:
            anio = int(anio)
        except ValueError:
            salida.insert(tk.END, "⚠️ El año debe ser un número.\n")
            return

        libro = Libro(titulo, autor, anio, salida)
        biblioteca.append(libro)

        # limpiar entradas
        entry_titulo.delete(0, tk.END)
        entry_autor.delete(0, tk.END)
        entry_anio.delete(0, tk.END)
    else:
        salida.insert(tk.END, "⚠️ Complete todos los campos.\n")


def mostrar_libros():
    if biblioteca:
        for libro in biblioteca:
            libro.mostrar_informacion()
    else:
        salida.insert(tk.END, "⚠️ No hay libros en la biblioteca.\n")


def eliminar_libros():
    biblioteca.clear()
    gc.collect()
    salida.insert(tk.END, "Todos los libros fueron eliminados.\n")


# Interfaz Tkinter
root = tk.Tk()
root.title("Gestión de Biblioteca")
root.geometry("500x500")

# Entradas de datos
tk.Label(root, text="Título:").pack()
entry_titulo = tk.Entry(root, width=40)
entry_titulo.pack()

tk.Label(root, text="Autor:").pack()
entry_autor = tk.Entry(root, width=40)
entry_autor.pack()

tk.Label(root, text="Año:").pack()
entry_anio = tk.Entry(root, width=40)
entry_anio.pack()

# Botones
btn_agregar = tk.Button(root, text="Agregar Libro", command=agregar_libro)
btn_agregar.pack(pady=5)

btn_mostrar = tk.Button(root, text="Mostrar Libros", command=mostrar_libros)
btn_mostrar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Libros", command=eliminar_libros)
btn_eliminar.pack(pady=5)

# Área de salida
salida = tk.Text(root, height=15, width=60)
salida.pack(pady=10)

root.mainloop()
