class pajaro:
    def mover(self):
        print("El pajaro vuela")

class pez:
    def mover(self):
        print("El pez nada")

class persona:
    def mover(self):
        print("La persona camina")

def desplazar(objeto):
    objeto.mover()

objetos = [pajaro(),pez(),persona()]

for objeto in objetos:
    desplazar(objeto)
    
