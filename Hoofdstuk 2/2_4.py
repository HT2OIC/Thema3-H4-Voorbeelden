import numpy as np
import matplotlib.pyplot as plt

# Grafiek aanmaken
t = np.linspace(0, 1.5, 1000)  # 1000 punten tussen 0 en 20
snelheid = 10
hoek = np.radians(45)
x = snelheid * np.cos(hoek) * t
y = snelheid * np.sin(hoek) * t - (9.81 * t**2)/2
plt.plot(x, y)

# titel en labels
plt.xlabel("Afstand (m)")
plt.ylabel("Hoogte (m)")
plt.title("Schuine worp")

# Grafiek tonen
plt.show()