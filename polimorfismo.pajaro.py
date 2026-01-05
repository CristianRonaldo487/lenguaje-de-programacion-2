class pajaro:
    def volar(self):
        print("El pajaro vuela")

class avion:
    def volar(self):
        print("el avion vuela")

def hacer_volar(obj):
    obj.volar()
hacer_volar(pajaro())
hacer_volar(avion())
    
