import math
class Comida:
    def __int__(self, proteinas,carbohidratos,grasas):
        self.proteinas = proteinas
        self.carbohidratos = carbohidratos
        self.grasas = grasas
        print("objeto comida creado")
        print(f"{self.proteinas}g {self.carbohidratos}g {self.grasas}g")


    def calcular_calorias(self):
        calorias = {self.proteinas *4 + self.carbohidratos *4 + self.grasas *9}
        return calorias
    
    def mostrar_informacion(self):
        print("Informacion Nutricional")
        print(f"Proteinas {self.proteinas}")
        print(f"carbohidratos :{self.carbohidratos}")
        print(f"grasas : {self.grasas}")
        print(f"calorias totales : {self.calcular_calorias()}")
        
almuerzo = Comida(proteinas=30, carbohidratos=50, grasas=20)
almuerzo.mostrar_informacion()       
