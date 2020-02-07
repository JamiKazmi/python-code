import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
s = np.sin(x)
c = np.cos(x)
t = np.tan(x)

plt.plot(s)
plt.plot(c)
plt.plot(t)
plt.show()
