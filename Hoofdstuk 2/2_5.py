import numpy as np
import matplotlib.pyplot as plt

# Grafiek maken
x = np.linspace(0, 20, 1000)  # 1000 punten tussen 0 en 20
y = 2*x + 5
plt.plot(x, y)

# limieten instellen
plt.xlim(0, 10)
plt.ylim(0, 20)

# Grafiek tonen
plt.show()