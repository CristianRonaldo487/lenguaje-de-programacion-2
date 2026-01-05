import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        self.disponible = True
        return True

class Prestamo:
    def __init__(self, libro, fecha_prestamo, usuario):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.usuario = usuario
        self.devuelto = False

    def marcar_devolucion(self):
        self.devuelto = True
        self.libro.devolver()

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []

    def realizar_prestamo(self, libro, fecha):
        if libro.disponible:
            if libro.prestar():
                prestamo = Prestamo(libro, fecha, self)
                self.prestamos.append(prestamo)
                return True
        return False

class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.root.geometry("800x600")
        
        # Listas para almacenar datos
        self.libros = []
        self.usuarios = []
        self.prestamos_activos = []
        
        # Crear algunos datos de ejemplo
        self.crear_datos_ejemplo()
        
        # Crear interfaz
        self.crear_interfaz()
    
    def crear_datos_ejemplo(self):
        # Libros de ejemplo
        self.libros.extend([
            Libro("Cien años de soledad", "Gabriel García Márquez", "12345"),
            Libro("El Principito", "Antoine de Saint-Exupéry", "98765"),
            Libro("1984", "George Orwell", "54321")
        ])
        
        # Usuarios de ejemplo
        self.usuarios.extend([
            Usuario("Juan Perez", "U001"),
            Usuario("María García", "U002")
        ])
    
    def crear_interfaz(self):
        # Notebook (pestañas)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Pestaña de Libros
        self.crear_pestana_libros(notebook)
        
        # Pestaña de Usuarios
        self.crear_pestana_usuarios(notebook)
        
        # Pestaña de Préstamos
        self.crear_pestana_prestamos(notebook)
        
        # Pestaña de Información
        self.crear_pestana_informacion(notebook)
    
    def crear_pestana_libros(self, notebook):
        # Frame para libros
        frame_libros = ttk.Frame(notebook)
        notebook.add(frame_libros, text="Gestión de Libros")
        
        # Formulario para agregar libros
        frame_formulario = ttk.LabelFrame(frame_libros, text="Agregar Nuevo Libro", padding=10)
        frame_formulario.pack(fill='x', padx=5, pady=5)
        
        # Campos del formulario
        ttk.Label(frame_formulario, text="Título:").grid(row=0, column=0, sticky='w', padx=5, pady=2)
        self.entry_titulo = ttk.Entry(frame_formulario, width=30)
        self.entry_titulo.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(frame_formulario, text="Autor:").grid(row=1, column=0, sticky='w', padx=5, pady=2)
        self.entry_autor = ttk.Entry(frame_formulario, width=30)
        self.entry_autor.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Label(frame_formulario, text="ISBN:").grid(row=2, column=0, sticky='w', padx=5, pady=2)
        self.entry_isbn = ttk.Entry(frame_formulario, width=30)
        self.entry_isbn.grid(row=2, column=1, padx=5, pady=2)
        
        # Botones
        frame_botones = ttk.Frame(frame_formulario)
        frame_botones.grid(row=3, column=0, columnspan=2, pady=10)
        
        ttk.Button(frame_botones, text="Agregar Libro", 
                  command=self.agregar_libro).pack(side='left', padx=5)
        ttk.Button(frame_botones, text="Limpiar Campos", 
                  command=self.limpiar_campos_libro).pack(side='left', padx=5)
        
        # Lista de libros
        frame_lista = ttk.LabelFrame(frame_libros, text="Lista de Libros", padding=10)
        frame_lista.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Treeview para mostrar libros
        columns = ('Título', 'Autor', 'ISBN', 'Disponible')
        self.tree_libros = ttk.Treeview(frame_lista, columns=columns, show='headings')
        
        # Configurar columnas
        for col in columns:
            self.tree_libros.heading(col, text=col)
            self.tree_libros.column(col, width=150)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_lista, orient='vertical', command=self.tree_libros.yview)
        self.tree_libros.configure(yscrollcommand=scrollbar.set)
        
        self.tree_libros.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Actualizar lista de libros
        self.actualizar_lista_libros()
    
    def crear_pestana_usuarios(self, notebook):
        frame_usuarios = ttk.Frame(notebook)
        notebook.add(frame_usuarios, text="Gestión de Usuarios")
        
        # Formulario para usuarios
        frame_formulario = ttk.LabelFrame(frame_usuarios, text="Agregar Nuevo Usuario", padding=10)
        frame_formulario.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(frame_formulario, text="Nombre:").grid(row=0, column=0, sticky='w', padx=5, pady=2)
        self.entry_nombre_usuario = ttk.Entry(frame_formulario, width=30)
        self.entry_nombre_usuario.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(frame_formulario, text="ID Usuario:").grid(row=1, column=0, sticky='w', padx=5, pady=2)
        self.entry_id_usuario = ttk.Entry(frame_formulario, width=30)
        self.entry_id_usuario.grid(row=1, column=1, padx=5, pady=2)
        
        frame_botones = ttk.Frame(frame_formulario)
        frame_botones.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(frame_botones, text="Agregar Usuario", 
                  command=self.agregar_usuario).pack(side='left', padx=5)
        
        # Lista de usuarios
        frame_lista = ttk.LabelFrame(frame_usuarios, text="Lista de Usuarios", padding=10)
        frame_lista.pack(fill='both', expand=True, padx=5, pady=5)
        
        columns = ('Nombre', 'ID Usuario')
        self.tree_usuarios = ttk.Treeview(frame_lista, columns=columns, show='headings')
        
        for col in columns:
            self.tree_usuarios.heading(col, text=col)
            self.tree_usuarios.column(col, width=200)
        
        scrollbar = ttk.Scrollbar(frame_lista, orient='vertical', command=self.tree_usuarios.yview)
        self.tree_usuarios.configure(yscrollcommand=scrollbar.set)
        
        self.tree_usuarios.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.actualizar_lista_usuarios()
    
    def crear_pestana_prestamos(self, notebook):
        frame_prestamos = ttk.Frame(notebook)
        notebook.add(frame_prestamos, text="Gestión de Préstamos")
        
        # Frame para realizar préstamo
        frame_realizar = ttk.LabelFrame(frame_prestamos, text="Realizar Préstamo", padding=10)
        frame_realizar.pack(fill='x', padx=5, pady=5)
        
        ttk.Label(frame_realizar, text="Usuario:").grid(row=0, column=0, sticky='w', padx=5, pady=2)
        self.combo_usuario = ttk.Combobox(frame_realizar, state="readonly", width=27)
        self.combo_usuario.grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(frame_realizar, text="Libro:").grid(row=1, column=0, sticky='w', padx=5, pady=2)
        self.combo_libro = ttk.Combobox(frame_realizar, state="readonly", width=27)
        self.combo_libro.grid(row=1, column=1, padx=5, pady=2)
        
        ttk.Button(frame_realizar, text="Realizar Préstamo", 
                  command=self.realizar_prestamo).grid(row=2, column=0, columnspan=2, pady=10)
        
        # Frame para préstamos activos
        frame_activos = ttk.LabelFrame(frame_prestamos, text="Préstamos Activos", padding=10)
        frame_activos.pack(fill='both', expand=True, padx=5, pady=5)
        
        columns = ('Usuario', 'Libro', 'Fecha Préstamo')
        self.tree_prestamos = ttk.Treeview(frame_activos, columns=columns, show='headings')
        
        for col in columns:
            self.tree_prestamos.heading(col, text=col)
            self.tree_prestamos.column(col, width=150)
        
        scrollbar = ttk.Scrollbar(frame_activos, orient='vertical', command=self.tree_prestamos.yview)
        self.tree_prestamos.configure(yscrollcommand=scrollbar.set)
        
        self.tree_prestamos.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Botón para devolución
        ttk.Button(frame_activos, text="Marcar como Devuelto", 
                  command=self.marcar_devolucion).pack(pady=5)
        
        self.actualizar_combos()
        self.actualizar_lista_prestamos()
    
    def crear_pestana_informacion(self, notebook):
        frame_info = ttk.Frame(notebook)
        notebook.add(frame_info, text="Información General")
        
        # Estadísticas
        frame_stats = ttk.LabelFrame(frame_info, text="Estadísticas", padding=10)
        frame_stats.pack(fill='x', padx=5, pady=5)
        
        self.label_stats = ttk.Label(frame_stats, text="", font=('Arial', 10))
        self.label_stats.pack(anchor='w')
        
        # Información detallada
        frame_detalle = ttk.LabelFrame(frame_info, text="Detalles", padding=10)
        frame_detalle.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.text_detalle = tk.Text(frame_detalle, height=15, width=80)
        scrollbar = ttk.Scrollbar(frame_detalle, orient='vertical', command=self.text_detalle.yview)
        self.text_detalle.configure(yscrollcommand=scrollbar.set)
        
        self.text_detalle.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        ttk.Button(frame_detalle, text="Actualizar Información", 
                  command=self.actualizar_informacion).pack(pady=5)
        
        self.actualizar_informacion()
    
    def agregar_libro(self):
        titulo = self.entry_titulo.get().strip()
        autor = self.entry_autor.get().strip()
        isbn = self.entry_isbn.get().strip()
        
        if not titulo or not autor or not isbn:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        # Verificar si el ISBN ya existe
        for libro in self.libros:
            if libro.isbn == isbn:
                messagebox.showerror("Error", "El ISBN ya existe")
                return
        
        nuevo_libro = Libro(titulo, autor, isbn)
        self.libros.append(nuevo_libro)
        
        messagebox.showinfo("Éxito", f"Libro '{titulo}' agregado correctamente")
        self.limpiar_campos_libro()
        self.actualizar_lista_libros()
        self.actualizar_combos()
    
    def limpiar_campos_libro(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_isbn.delete(0, tk.END)
    
    def agregar_usuario(self):
        nombre = self.entry_nombre_usuario.get().strip()
        id_usuario = self.entry_id_usuario.get().strip()
        
        if not nombre or not id_usuario:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        # Verificar si el ID ya existe
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                messagebox.showerror("Error", "El ID de usuario ya existe")
                return
        
        nuevo_usuario = Usuario(nombre, id_usuario)
        self.usuarios.append(nuevo_usuario)
        
        messagebox.showinfo("Éxito", f"Usuario '{nombre}' agregado correctamente")
        self.entry_nombre_usuario.delete(0, tk.END)
        self.entry_id_usuario.delete(0, tk.END)
        self.actualizar_lista_usuarios()
        self.actualizar_combos()
    
    def realizar_prestamo(self):
        usuario_idx = self.combo_usuario.current()
        libro_idx = self.combo_libro.current()
        
        if usuario_idx == -1 or libro_idx == -1:
            messagebox.showerror("Error", "Seleccione usuario y libro")
            return
        
        usuario = self.usuarios[usuario_idx]
        libro = self.libros[libro_idx]
        
        if not libro.disponible:
            messagebox.showerror("Error", "El libro no está disponible")
            return
        
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        if usuario.realizar_prestamo(libro, fecha_actual):
            self.prestamos_activos.append(usuario.prestamos[-1])
            messagebox.showinfo("Éxito", f"Préstamo realizado: {libro.titulo} a {usuario.nombre}")
            self.actualizar_lista_libros()
            self.actualizar_lista_prestamos()
            self.actualizar_combos()
        else:
            messagebox.showerror("Error", "No se pudo realizar el préstamo")
    
    def marcar_devolucion(self):
        seleccion = self.tree_prestamos.selection()
        if not seleccion:
            messagebox.showerror("Error", "Seleccione un préstamo")
            return
        
        item = seleccion[0]
        idx = self.tree_prestamos.index(item)
        
        if idx < len(self.prestamos_activos):
            prestamo = self.prestamos_activos[idx]
            prestamo.marcar_devolucion()
            self.prestamos_activos.remove(prestamo)
            
            messagebox.showinfo("Éxito", f"Libro '{prestamo.libro.titulo}' devuelto")
            self.actualizar_lista_libros()
            self.actualizar_lista_prestamos()
            self.actualizar_combos()
    
    def actualizar_lista_libros(self):
        self.tree_libros.delete(*self.tree_libros.get_children())
        for libro in self.libros:
            disponible = "Sí" if libro.disponible else "No"
            self.tree_libros.insert('', 'end', values=(libro.titulo, libro.autor, libro.isbn, disponible))
    
    def actualizar_lista_usuarios(self):
        self.tree_usuarios.delete(*self.tree_usuarios.get_children())
        for usuario in self.usuarios:
            self.tree_usuarios.insert('', 'end', values=(usuario.nombre, usuario.id_usuario))
    
    def actualizar_lista_prestamos(self):
        self.tree_prestamos.delete(*self.tree_prestamos.get_children())
        for prestamo in self.prestamos_activos:
            self.tree_prestamos.insert('', 'end', 
                                     values=(prestamo.usuario.nombre, 
                                             prestamo.libro.titulo, 
                                             prestamo.fecha_prestamo))
    
    def actualizar_combos(self):
        # Actualizar combo de usuarios
        usuarios_list = [f"{usuario.nombre} ({usuario.id_usuario})" for usuario in self.usuarios]
        self.combo_usuario['values'] = usuarios_list
        
        # Actualizar combo de libros (solo disponibles)
        libros_disponibles = [libro.titulo for libro in self.libros if libro.disponible]
        self.combo_libro['values'] = libros_disponibles
        
        if usuarios_list:
            self.combo_usuario.current(0)
        if libros_disponibles:
            self.combo_libro.current(0)
    
    def actualizar_informacion(self):
        # Actualizar estadísticas
        total_libros = len(self.libros)
        libros_disponibles = sum(1 for libro in self.libros if libro.disponible)
        total_usuarios = len(self.usuarios)
        prestamos_activos = len(self.prestamos_activos)
        
        stats_text = f"""
        Total de Libros: {total_libros}
        Libros Disponibles: {libros_disponibles}
        Libros Prestados: {total_libros - libros_disponibles}
        Total de Usuarios: {total_usuarios}
        Préstamos Activos: {prestamos_activos}
        """
        self.label_stats.config(text=stats_text)
        
        # Actualizar información detallada
        self.text_detalle.delete(1.0, tk.END)
        
        info_text = "=== LIBROS ===\n"
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            info_text += f"- {libro.titulo} por {libro.autor} ({estado})\n"
        
        info_text += "\n=== USUARIOS ===\n"
        for usuario in self.usuarios:
            info_text += f"- {usuario.nombre} (ID: {usuario.id_usuario})\n"
            if usuario.prestamos:
                info_text += "  Préstamos:\n"
                for prestamo in usuario.prestamos:
                    estado = "Devuelto" if prestamo.devuelto else "Pendiente"
                    info_text += f"  · {prestamo.libro.titulo} - {prestamo.fecha_prestamo} ({estado})\n"
        
        self.text_detalle.insert(1.0, info_text)

def main():
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
