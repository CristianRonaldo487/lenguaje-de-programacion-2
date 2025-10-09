import tkinter as tk
from tkinter import messagebox
import gc

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro registrado: {self.titulo}, {self.autor}, {self.anio}")

    def mostrar_informacion(self):
        return f"'{self.titulo}' fue escrito por {self.autor} en {self.anio}"

    def __del__(self):
        print(f"Libro eliminado: {self.titulo}")


# Lista de libros registrados
biblioteca = []


# ---- Funciones Tkinter ----
def registrar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()

    if not titulo or not autor or not anio:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    libro = Libro(titulo, autor, anio)
    biblioteca.append(libro)

    lista_libros.insert(tk.END, libro.mostrar_informacion())

    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)


def eliminar_todos():
    biblioteca.clear()
    lista_libros.delete(0, tk.END)
    gc.collect()
    messagebox.showinfo("Información", "Todos los libros fueron eliminados")


def eliminar_seleccionado():
    seleccionado = lista_libros.curselection()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Selecciona un libro para eliminar")
        return

    index = seleccionado[0]
    libro = biblioteca.pop(index)
    lista_libros.delete(index)
    del libro
    gc.collect()
    messagebox.showinfo("Información", "Libro eliminado correctamente")


# ---- Interfaz gráfica ----
root = tk.Tk()
root.title("Biblioteca - Registro de Libros")

# Etiquetas y entradas
tk.Label(root, text="Título:").grid(row=0, column=0, padx=5, pady=5)
entry_titulo = tk.Entry(root, width=30)
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Autor:").grid(row=1, column=0, padx=5, pady=5)
entry_autor = tk.Entry(root, width=30)
entry_autor.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Año:").grid(row=2, column=0, padx=5, pady=5)
entry_anio = tk.Entry(root, width=30)
entry_anio.grid(row=2, column=1, padx=5, pady=5)

# Botones
btn_registrar = tk.Button(root, text="Registrar", command=registrar_libro)
btn_registrar.grid(row=3, column=0, columnspan=2, pady=10)

btn_eliminar = tk.Button(root, text="Eliminar todos", command=eliminar_todos)
btn_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

btn_eliminar_sel = tk.Button(root, text="Eliminar seleccionado", command=eliminar_seleccionado)
btn_eliminar_sel.grid(row=5, column=0, columnspan=2, pady=5)

# Lista de libros
lista_libros = tk.Listbox(root, width=60, height=10)
lista_libros.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
