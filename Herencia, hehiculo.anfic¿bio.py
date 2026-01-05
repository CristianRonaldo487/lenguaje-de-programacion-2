class VehiculoTerrestre:
    def conducir(self):
        print("Conduciendo por la carretera...")

    def frenar(self):
        print("El vehículo terrestre se ha detenido.")


class VehiculoAcuatico:
    def navegar(self):
        print("Navegando por el agua...")

    def fondear(self):
        print("El vehículo acuático ha fondeado.")


class VehiculoAnfibio(VehiculoTerrestre, VehiculoAcuatico):
    def transformar(self, modo):
        if modo.lower() == "tierra":
            print("Cambiando al modo terrestre...")
        elif modo.lower() == "agua":
            print("Cambiando al modo acuático...")
        else:
            print("Modo no reconocido.")


def main():
    anfibio = VehiculoAnfibio()

    anfibio.transformar("tierra")
    anfibio.conducir()
    anfibio.frenar()

    print("\n")

    anfibio.transformar("agua")
    anfibio.navegar()
    anfibio.fondear()


if __name__ == "__main__":
    main()
