import numpy as np
import matplotlib.pyplot as plt

print("Graficador de funciones lineales")

# Rango de x
x = np.linspace(-10, 10, 1000)

# Pedir funciones al usuario
f1 = input("Ingresa la primera función: ")
f2 = input("Ingresa la segunda función: ")

# Calcular valores
y1 = eval(f1, {"np": np, "x": x})
y2 = eval(f2, {"np": np, "x": x})

# Graficar
plt.plot(x, y1, label=f1)
plt.plot(x, y2, label=f2)

# Ejes
plt.axhline(0, color="black", linewidth=0.7)
plt.axvline(0, color="black", linewidth=0.7)

plt.legend()
plt.grid(True)
plt.show()
