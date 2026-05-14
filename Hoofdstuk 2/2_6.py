import numpy as np
import matplotlib.pyplot as plt

# Punten grafiek bepalen
x = np.linspace(0, 10, 500)
y = np.sin(x)

# Punten plotten met als stijl: stip-lijn en rood
plt.plot(x, y, "-.r")

# Labels en titel
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sinus")

# Grafiek tonen
plt.show()