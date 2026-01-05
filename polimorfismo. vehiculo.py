class vehiculo:
    def iniciar(self):
        print("El vehiculo esta listo para  moverse")

class coche(vehiculo):
    def iniciar(self):
        print("El coche arranca y celera")

class bicicleta(vehiculo):
    def iniciar(self):
        print("La bicicleta empieza a pedalear")

class barco(vehiculo):
    def iniciar(self):
        print("El barco enciende el motor y zarpa")

vehiculos = [coche(),bicicleta(),barco()]

for v in vehiculos:
    v.iniciar()

    
        
