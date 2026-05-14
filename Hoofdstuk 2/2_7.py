import numpy as np
import matplotlib.pyplot as plt

# Grafieken aanmaken
x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)

# Grafieken plotten met labels
plt.plot(x, y1, "-b", label="sinus")
plt.plot(x, y2, "-.r", label="cosinus")

# Legenda rechtsboven toevoegen
plt.legend(loc="upper right")

# Titel en assen benoemen
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sinus en cosinus")

# Grafiek tonen
plt.show()