class GestorTareas:
    def __init(self):
        self.tareas = []

    def agregar_tarea(self,tarea):
        self.tareas.append(tareas)
        print("tareaa agregada")

    def mostrar_tareas(self):
        if not sself.tareas:
            print("No hay tareas pendientes")
        else:
            print("tareas pendientes")
            for i, tarea in enumerate(self.tareas,1):
                print(f"{i} {tarea}")

mi_gestor = GestorTareas()

while True:
    print("\n ---- MENU---")
    print("1. Agregar tarea ")
    print("2. Mostrar tareas ")
    print("3. Salir")
    opcion = input("seleccione una ipcion")

    if opcion == "1":
        tarea = input ("Escribe la tarea: ")
        mi_gestor.agregar_tarea(tarea)
    elif opcion == "2":
       mi_gestor.mostrar_tareas()
    elif opcion == "3":
        print("Saliendo del gestor de tareas: ")
        break
    else:
        print("opcion no valida. Intente de nuevo")
    

            
