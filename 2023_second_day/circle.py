import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1, 1, 1000)

y1 = np.sqrt(1 - x**2)
y2 = -y1

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()
