class Persona:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre      
        self.dia = dia            
        self.mes = mes            
        self.signo = self.obtener_signo()  

    def obtener_signo(self):
        """Devuelve el signo zodiacal según la fecha de nacimiento"""
        if (self.mes == 3 and self.dia >= 21) or (self.mes == 4 and self.dia <= 19):
            return "Aries"
        elif (self.mes == 4 and self.dia >= 20) or (self.mes == 5 and self.dia <= 20):
            return "Tauro"
        elif (self.mes == 5 and self.dia >= 21) or (self.mes == 6 and self.dia <= 20):
            return "Géminis"
        elif (self.mes == 6 and self.dia >= 21) or (self.mes == 7 and self.dia <= 22):
            return "Cáncer"
        elif (self.mes == 7 and self.dia >= 23) or (self.mes == 8 and self.dia <= 22):
            return "Leo"
        elif (self.mes == 8 and self.dia >= 23) or (self.mes == 9 and self.dia <= 22):
            return "Virgo"
        elif (self.mes == 9 and self.dia >= 23) or (self.mes == 10 and self.dia <= 22):
            return "Libra"
        elif (self.mes == 10 and self.dia >= 23) or (self.mes == 11 and self.dia <= 21):
            return "Escorpio"
        elif (self.mes == 11 and self.dia >= 22) or (self.mes == 12 and self.dia <= 21):
            return "Sagitario"
        elif (self.mes == 12 and self.dia >= 22) or (self.mes == 1 and self.dia <= 19):
            return "Capricornio"
        elif (self.mes == 1 and self.dia >= 20) or (self.mes == 2 and self.dia <= 18):
            return "Acuario"
        elif (self.mes == 2 and self.dia >= 19) or (self.mes == 3 and self.dia <= 20):
            return "Piscis"
        else:
            return "Fecha inválida"

    def mostrar_info(self):
        """Muestra la información de la persona"""
        print(f"Hola {self.nombre}, naciste el {self.dia}/{self.mes} y tu signo es {self.signo}.")


nombre = input("Ingresa tu nombre: ")
dia = int(input("Ingresa tu día de nacimiento (1-31): "))
mes = int(input("Ingresa tu mes de nacimiento (1-12): "))

persona1 = Persona(nombre, dia, mes)  
persona1.mostrar_info()
