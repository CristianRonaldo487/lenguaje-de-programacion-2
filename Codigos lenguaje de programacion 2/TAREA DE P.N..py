import matplotlib.pyplot as plt
import numpy as np

# Pedir datos al usuario
m = float(input("Ingresa la pendiente (m): "))
b = float(input("Ingresa la intersección con el eje Y (b): "))
rango = float(input("Ingresa el rango de valores para x (ejemplo 10): "))

# Definir los valores de x
x = np.linspace(-rango, rango, 200)  # desde -rango hasta rango, con 200 puntos

# Ecuación de la recta
y = m * x + b

# Crear la gráfica
plt.figure(figsize=(6,4))
plt.plot(x, y, label=f"y = {m}x + {b}", color="blue")

# Agregar ejes
plt.axhline(0, color="black", linewidth=0.8)  # eje X
plt.axvline(0, color="black", linewidth=0.8)  # eje Y

# Agregar título y etiquetas
plt.title("Gráfico de una Función Lineal")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()
