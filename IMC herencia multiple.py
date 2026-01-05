class Peso:
    def __init__ (self, peso_kg):
        self.peso_kg=peso_kg

class Altura:
    def __init__ (self, altura_m):
        self.altura_m=altura_m


class IMC(Peso, Altura):
    def __init__ (self, peso_kg, altura_m):
        Peso.__init__(self, peso_kg)
        Altura.__init__(self, altura_m)

    def calcularimc(self):
        if self.altura_m <= 0:
            raise ValueError("La altura debe mayor que cero")
        return self.peso_kg/(self.altura_m**2)
    def categoria(self):
        imc = self.calcularimc()
        if imc < 18.5:
            return "Bajo Peso"
        elif 18.5<=imc<25:
            return "Normal"
        elif 25<=imc<=30:
            return "Sobrepeso"
        else:
            return "Obesidad"
    def mostrar(self):
        imc = self.calcularimc()
        categoria = self.categoria()
        return f"Indice de masa: {imc:2f} Categoria: {categoria}"

def leer_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <=0:
                print("Ingrese un valor positivo")
                continue
            return valor
        except ValueError:
            print("Entrada Invalida")

peso = leer_float("Ingrese su peso en KG:")
altura = leer_float("Ingrese la altura en M:")


persona= IMC(peso_kg=peso, altura_m=altura)
print(persona.mostrar())
