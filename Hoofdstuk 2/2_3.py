import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 20, 1000)  # 1000 punten tussen 0 en 20
y = np.sin(x)

plt.plot(x, y)
plt.show()