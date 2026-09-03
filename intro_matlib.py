import numpy as np
import matplotlib.pyplot as plt

stress = np.array([0, 50, 100, 150, 180, 190])
strain = np.array([0, 0.001, 0.002, 0.003, 0.004, 0.005])

plt.plot(stress, strain, marker = "o")
plt.xlabel("Stress")
plt.ylabel("Strain")
plt.title("Stress - Strain Curve")
plt.grid(True)
plt.show()
