import numpy as np
import matplotlib.pyplot as plt  #importing matplotlib.pyplot     

stress = np.array([0, 50, 100, 150, 180, 190])   #assigning values
strain = np.array([0, 0.001, 0.002, 0.003, 0.004, 0.005])

plt.plot(stress, strain, marker = "o")           
plt.xlabel("Stress")             #assigning x and y lines 
plt.ylabel("Strain")
plt.title("Stress - Strain Curve")
plt.grid(True)      #Using grid lines
plt.show()      
