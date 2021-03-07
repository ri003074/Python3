import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.subplot(2, 2, 1)
plt.plot(x, y1)

plt.subplot(2, 2, 2)
plt.plot(x, y2)

plt.subplot(2, 2, 3)
plt.plot(x, y1)

plt.subplot(2, 2, 4)
plt.plot(x, y2)
plt.show()
