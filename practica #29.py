class libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print("{self.titulo} de {self.autor} creado")

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")

    def __del__(self):
        print(f"Libro '{self.titulo}' eliminado de la biblioteca.")


libro1 = Libro("Cien años de soledad", "Gabriel Garcia Márquez", 1967)
libro1.mostrar_info()
        
        


        
         

        
        
    
    
