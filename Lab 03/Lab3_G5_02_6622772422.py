import numpy as np
import matplotlib.pyplot as plt
import math as m

x = np.arange(0, 10, 0.1)
y = (1+x)/(np.sqrt(x))

plt.plot(x, y, color="blue", linewidth=2, linestyle= "dotted")
plt.show()
