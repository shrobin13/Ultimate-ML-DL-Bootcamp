
import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(1, 50, 50)
y = x

plt.plot(x, y)
plt.savefig("plot.png")
