class Temperatura:
    def __init__(self, fahrenheit):
        self.f = fahrenheit

    def a_celsius(self):
        return (self.f - 32) * 5 / 9


# Uso
f = float(input("Temperatura en Fahrenheit: "))
t = Temperatura(f)
print(f"{t.f} °F = {t.a_celsius():.2f} °C")
