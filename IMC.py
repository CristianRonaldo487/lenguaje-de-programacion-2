class Persona:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def imc(self):
        return self.peso / (self.altura ** 2)

    def clasificacion(self):
        imc = self.imc()
        if imc < 18.5:
            return "Bajo peso"
        elif imc <= 24.9:
            return "Normal"
        elif imc <= 29.9:
            return "Sobrepeso"
        elif imc <= 34.9:
            return "Obesidad grado I"
        elif imc <= 39.9:
            return "Obesidad grado II"
        else:
            return "Obesidad grado III (mórbida)"
        
peso = float(input("Ingrese peso: "))
altura = float(input("ingrese altuira: "))

persona = Persona(peso, altura)

print("IMC:", round(persona.imc(), 2))
print("Clasificación:", persona.clasificacion())
