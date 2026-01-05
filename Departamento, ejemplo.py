class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.departamentos = [] 

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

dep1 = Departamento("Ingeniería Estadística")
dep2 = Departamento("Informática")

uni = Universidad("Universidad Nacional del Altiplano")
uni.agregar_departamento(dep1)
uni.agregar_departamento(dep2)

for d in uni.departamentos:
    print(d.nombre)

    
