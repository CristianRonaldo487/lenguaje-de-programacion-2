import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.bar(destinos, dist_estacionaria*100)
plt.ylabel("Porcentaje de turistas (%)")
plt.title("Distribución Estacionaria de Turistas")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig("distribucion_estacionaria.png", dpi=300)
plt.show()



