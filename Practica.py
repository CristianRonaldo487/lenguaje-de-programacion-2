class Persona:
    def __init__(self, peso, altura):
        self.peso = peso      
        self.altura = altura  

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def clasificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Bajo peso"
        elif 18.5 <= imc <= 24.9:
            return "Normal"
        elif 25.0 <= imc <= 29.9:
            return "Sobrepeso"
        elif 30.0 <= imc <= 34.9:
            return "Obesidad grado I"
        elif 35.0 <= imc <= 39.9:
            return "Obesidad grado II"
        else:
            return "Obesidad grado III (mórbida)"


# Objeto
persona1 = Persona(70, 1.75)  
print(f"IMC: {persona1.calcular_imc():.2f}")
print("Clasificación:", persona1.clasificar_imc())
