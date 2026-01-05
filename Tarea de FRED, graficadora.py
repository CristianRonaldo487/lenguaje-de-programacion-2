import numpy as np
import matplotlib.pyplot as plt

# === 1. Definir el rango de X ===
x_min = -10
x_max = 10
paso = 0.1
x = np.arange(x_min, x_max + paso, paso)

# === 2. Definir las funciones lineales ===
# Puedes cambiar estas funciones
def f1(x):
    return 2 * x + 3

def f2(x):
    return -x + 5

# === 3. Evaluar las funciones ===
y1 = f1(x)
y2 = f2(x)

# === 4. Graficar ===
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label="f1(x) = 2x + 3", color="blue", marker='o', markersize=3)
plt.plot(x, y2, label="f2(x) = -x + 5", color="red", marker='x', markersize=3)

# Opcional: Dibujar el eje X y Y
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Configuración del gráfico
plt.title("Gráfica de dos funciones lineales")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
