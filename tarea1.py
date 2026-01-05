class SignoZodiacal:
    def __init__(self, dia, mes):
        self.dia = dia
        self.mes = mes

    def mostrar_signo(self):
        dia = self.dia
        mes = self.mes

        if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
            return "Aries"
        elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
            return "Tauro"
        elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
            return "Géminis"
        elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
            return "Cáncer"
        elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
            return "Leo"
        elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
            return "Virgo"
        elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 23):
            return "Libra"
        elif (mes == 10 and dia >= 24) or (mes == 11 and dia <= 22):
            return "Escorpio"
        elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
            return "Sagitario"
        elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
            return "Capricornio"
        elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
            return "Acuario"
        elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
            return "Piscis"


print("signo zodiacal")

# pedir datos al usuario
dia = int(input("Ingresa tu día de nacimiento entre (1 a 31): "))
mes = int(input("Ingresa tu mes de nacimiento entre (1 a 12): "))


persona = SignoZodiacal(dia, mes)

# mostrar signo
print(f"Tu signo zodiacal es: {persona.mostrar_signo()}")

